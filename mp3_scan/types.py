from pydantic import BaseModel

class Mp3Item(BaseModel):
    """represents an mp3 item detected within a target mp3 folder"""

    folder:str
    name:str

    path:str

class DecisionItem(BaseModel):
    """temp obj representing decision item made by user from google sheets"""

    decision:str
    folder:str
    filename:str
