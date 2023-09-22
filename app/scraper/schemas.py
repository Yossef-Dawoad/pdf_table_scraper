from pydantic import BaseModel


class ScrapedData(BaseModel):
    name: str
    party: str
    postion: str
