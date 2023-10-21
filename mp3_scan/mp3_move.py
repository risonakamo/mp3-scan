# functions executing mp3 move

from os import makedirs
from os.path import dirname,join,basename
from shutil import move

from mp3_scan.types import DecisionItem, DecisionItemPair


def doMp3Move(decision:DecisionItemPair)->None:
    """execute decision item. moves target mp3 into a folder named after the decision item
    in the immediate folder where the mp3 is located"""

    # target folder is a folder named after the decision right next to the mp3 file
    decisionDirPath:str=join(
        dirname(decision.mp3item.path),
        decision.decision.decision
    )

    makedirs(decisionDirPath,exist_ok=True)

    move(
        decision.mp3item.path,
        decisionDirPath
    )

def doAllMp3Move(pairs:list[DecisionItemPair])->None:
    """list version of mp3 move"""

    for pair in pairs:
        pair:DecisionItemPair
        doMp3Move(pair)