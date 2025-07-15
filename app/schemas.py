from pydantic import BaseModel

class UrlCreate(BaseModel):
    url: str
