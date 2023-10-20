# functions that interact with mp3 items

from os.path import join,basename,dirname,splitext
from glob import glob
from loguru import logger
from rich import print as printr

from mp3_scan.types import Mp3Item


def scanMp3Dir(
    dir:str,
    ignoredParentDirs:set[str]=set()
)->list[Mp3Item]:
    """scan a dir for all mp3 items inside. give set of parent dirs to ignore. ignored parent dir
    only considers the mp3's immediate parent"""

    allFilePaths:list[str]=glob(
        join(dir,"**/*.mp3"),
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

    printr(f"Discovered {len(filteredFilePaths)}/{len(allFilePaths)} items")
    printr()

    printAllParents(mp3items)
    printr()

    return mp3items

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

def mp3ItemToStr(item:Mp3Item)->str:
    """convert item to str for write-out"""

    return f"{item.folder}\t{item.name}"

def mp3ItemsToText(items:list[Mp3Item])->str:
    """convert list of mp3 items into text list"""

    text:str=""

    for item in items:
        item:Mp3Item

        text+=mp3ItemToStr(item)+"\n"

    return text

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