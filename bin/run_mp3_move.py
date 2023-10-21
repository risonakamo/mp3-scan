# do mp3 move actions using decision tsv as input

from devtools import debug
from os.path import join,dirname,realpath
from loguru import logger
from rich import print as printr

from mp3_scan.decision_tsv import pairDecisionItems, readDecisionTsv
from mp3_scan.mp3_item import scanMp3Dir
from mp3_scan.mp3_move import doAllMp3Move, doMp3Move

from mp3_scan.types import DecisionItem, DecisionItemPair, Mp3Item

HERE:str=dirname(realpath(__file__))

# ---- CONFIG ----
ignoredParentDirs:set[str]={
    "y",
    "n",
    "m"
}
"""if an item's parent dir matches one of these exactly, ignore the item"""

targetDir:str=r"C:\Users\ktkm2\Desktop\song jobs\new 2023-10-14"
"""top level where mp3 folders are at. all mp3s under this location should have a parent
folder that makes sense"""

decisionTsv:str=join(HERE,"../test/test-decision.tsv")
# ---- end CONFIG ----


@logger.catch()
def main():
    # get mp3 items
    items:list[Mp3Item]=scanMp3Dir(
        targetDir,
        ignoredParentDirs
    )

    # read from decision tsv
    decisions:list[DecisionItem]=readDecisionTsv(decisionTsv)

    # debug(items)
    # debug(decisions)

    pairs:list[DecisionItemPair]=pairDecisionItems(
        decisions,
        items
    )

    printr()
    printr("[cyan]executing move[/cyan]")
    doAllMp3Move(pairs)

if __name__=="__main__":
    main()