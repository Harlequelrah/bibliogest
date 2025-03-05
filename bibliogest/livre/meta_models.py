
from pydantic import BaseModel, Field


class MetaLivreModel(BaseModel):
    id:int
    titre:str
    contenue:str
    nbr_pages:int
    code_cat:str
