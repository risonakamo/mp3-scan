# functions dealing with decision tsv

from csv import DictReader
from devtools import debug as debugr

from loguru import logger
from mp3_scan.types import DecisionItem, DecisionItemPair, Mp3Item


def readDecisionTsv(filepath:str)->list[DecisionItem]:
    """read decision tsv into list of decision items"""

    items:list[DecisionItem]=[]
    with open(filepath,"r",encoding="utf-8") as rfile:
        for item in DictReader(rfile,delimiter="\t"):
            item:dict
            items.append(DecisionItem.model_validate(item))

    return items

def pairDecisionItems(decisions:list[DecisionItem],mp3items:list[Mp3Item])->list[DecisionItemPair]:
    """pair decision items with mp3 items"""

    pairs:list[DecisionItemPair]=[]

    # for all decisions, try to find its pair
    for decision in decisions:
        decision:DecisionItem

        foundPair:bool=False
        for mp3item in mp3items:
            mp3item:Mp3Item

            if (
                mp3item.folder==decision.folder
                and mp3item.name==decision.filename
            ):
                pairs.append(DecisionItemPair(
                    decision=decision,
                    mp3item=mp3item
                ))
                foundPair=True
                continue

        if not foundPair:
            logger.error("failed to find pair for:")
            debugr(decision)

    return pairs