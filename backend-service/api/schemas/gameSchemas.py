from pydantic import BaseModel
from datetime import datetime

class GameResponse(BaseModel):
    name: str
    cover: str