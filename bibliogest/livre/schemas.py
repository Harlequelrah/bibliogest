from typing import List, Optional
from pydantic import BaseModel, Field

from bibliogest.ecriture.meta_models import MetaEcritureModel




class LivreBaseModel(BaseModel):
    titre:str=Field(example="Merlin l'enchanteur")
    contenue:str=Field(example="Merlin l'enchanteur est un film de Walt Disney Pictures réalisé par Wolfgang Reitherman, sorti en 1963.")
    nbr_pages:int=Field(example=120)
    code_cat:str=Field(example="C0A1T2")


class LivreCreateModel(LivreBaseModel):
    pass

class LivreUpdateModel(LivreBaseModel):
    pass

class LivrePatchModel(BaseModel):
    titre:Optional[str]=Field(default=None,example="Merlin l'enchanteur")
    contenue:Optional[str]=Field(default=None,example="Merlin l'enchanteur est un film de Walt Disney Pictures réalisé par Wolfgang Reitherman, sorti en 1963.")
    nbr_pages:Optional[int]=Field(default=None,example=120)
    code_cat:Optional[str]=Field(default=None,example="C0A1T2")


class LivrePydanticModel(LivreBaseModel):
    id:int
    livres_ecritures : List["MetaEcritureModel"]=[]
    class Config:
        from_attributes=True


