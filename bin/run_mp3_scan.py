# run mp3 scan on target folder. output to csv file

from os.path import realpath
from loguru import logger
from rich import print as printr
from mp3_scan.mp3_tsv import writeMp3Csv

from mp3_scan.types import Mp3Item
from mp3_scan.mp3_item import scanMp3Dir,mp3ItemsToText

# ---- CONFIG ----
ignoredParentDirs:set[str]={
    "y",
    "n",
    "m"
}
"""if an item's parent dir matches one of these exactly, ignore the item"""

targetDir:str=r"E:\mp3\new\new 2023-10-14"
"""top level where mp3 folders are at. all mp3s under this location should have a parent
folder that makes sense"""
# ---- end CONFIG ----

@logger.catch()
def main():
    items:list[Mp3Item]=scanMp3Dir(
        targetDir,
        ignoredParentDirs
    )

    writePath:str=realpath("mp3-scan.csv")
    writeMp3Csv(items,writePath)

if __name__=="__main__":
    main()