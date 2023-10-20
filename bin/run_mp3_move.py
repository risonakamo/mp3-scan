from devtools import debug

from mp3_scan.decision_tsv import pairDecisionItems, readDecisionTsv
from mp3_scan.mp3_item import scanMp3Dir

from mp3_scan.types import DecisionItem, Mp3Item

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

decisionTsv:str=r"C:\Users\ktkm\Desktop\webpages\mp3-scan\test\decision-test.tsv"
# ---- end CONFIG ----


# get mp3 items
items:list[Mp3Item]=scanMp3Dir(
    targetDir,
    ignoredParentDirs
)

# read from decision tsv
decisions:list[DecisionItem]=readDecisionTsv(decisionTsv)

# debug(items)
# debug(decisions)

pairDecisionItems(
    decisions,
    items
)