# functions dealing with decision tsv

from csv import DictReader
from mp3_scan.types import DecisionItem


def readDecisionTsv(filepath:str)->list[DecisionItem]:
    """read decision tsv into list of decision items"""

    items:list[DecisionItem]=[]
    with open(filepath,"r") as rfile:
        for item in DictReader(rfile,delimiter="\t"):
            item:dict
            items.append(DecisionItem.model_validate(item))

    return items