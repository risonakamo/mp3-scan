from os.path import join,splitext,basename,dirname,realpath
from glob import glob
from devtools import debug
from pydantic import BaseModel
from loguru import logger
from rich import print as printr

# ---- CONFIG ----
ignoredParentDirs:set[str]={
    "y",
    "n",
    "m"
}
"""if an item's parent dir matches one of these exactly, ignore the item"""

targetDir:str=r"E:\mp3\new 2023-10-14"
"""top level where mp3 folders are at. all mp3s under this location should have a parent
folder that makes sense"""
# ---- end CONFIG ----

class Mp3Item(BaseModel):
    folder:str
    name:str

    path:str

def convertToMp3Item(file:str)->Mp3Item|None:
    """try to convert path of a file into mp3 item"""

    filenamePath:str
    extension:str

    filenamePath,extension=splitext(file)

    if extension!=".mp3":
        logger.warning("tried to convert item that is not mp3")

    return Mp3Item(
        folder=basename(dirname(filenamePath)),
        name=basename(filenamePath),
        path=file
    )

def printAllParents(mp3items:list[Mp3Item])->None:
    """print all parents seen"""

    parents:set[str]=set()

    for item in mp3items:
        item:Mp3Item

        parents.add(item.folder)

    printr("[cyan]All Parent Folders:[/cyan]")
    for parent in parents:
        parent:str

        printr("-",f"[yellow]{parent}[/yellow]")

def mp3ItemToStr(item:Mp3Item)->str:
    """convert item to str for write-out"""

    return f"{item.folder}; {item.name}"

def mp3ItemsToText(items:list[Mp3Item])->str:
    """convert list of mp3 items into text list"""

    text:str=""

    for item in items:
        item:Mp3Item

        text+=mp3ItemToStr(item)+"\n"

    return text

@logger.catch()
def main():
    allFilePaths:list[str]=glob(
        join(r"E:\mp3\new 2023-10-14","**/*.mp3"),
        recursive=True
    )

    filteredFilePaths:list[str]=[]

    # filter file paths
    for filepath in allFilePaths:
        filepath:str

        if basename(dirname(filepath)) not in ignoredParentDirs:
            filteredFilePaths.append(filepath)

    # generate mp3 items
    mp3items:list[Mp3Item]=[]

    for filepath in filteredFilePaths:
        filepath:str

        item:Mp3Item|None=convertToMp3Item(filepath)

        if item:
            mp3items.append(item)

    # debug(mp3items)

    printr(f"Discovered {len(filteredFilePaths)}/{len(allFilePaths)} items")
    printr()

    printAllParents(mp3items)
    printr()

    writePath:str=realpath("mp3-scan.csv")
    printr("Writing output to file:",writePath)
    with open(writePath,"w",encoding="utf-8") as wfile:
        wfile.write(mp3ItemsToText(mp3items))

if __name__=="__main__":
    main()