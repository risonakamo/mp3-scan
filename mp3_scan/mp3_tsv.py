# functions for dealing with mp3 tsv file

from rich import print as printr

from mp3_scan.mp3_item import mp3ItemsToText
from mp3_scan.types import Mp3Item


def writeMp3Csv(items:list[Mp3Item],outpath:str)->None:
    """write mp3 items to the output file (need extension)"""

    printr("Writing output to file:",outpath)
    with open(outpath,"w",encoding="utf-8") as wfile:
        wfile.write(mp3ItemsToText(items))