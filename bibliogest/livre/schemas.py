from typing import List, Optional
from pydantic import BaseModel, Field

from bibliogest.categorie.meta_models import MetaCategorieModel
from bibliogest.ecriture.meta_models import MetaEcritureModel




class LivreBaseModel(BaseModel):
    titre:str=Field(example="Merlin l'enchanteur")
    contenue:str=Field(example="Merlin l'enchanteur est un film de Walt Disney Pictures réalisé par Wolfgang Reitherman, sorti en 1963.")
    nbr_pages:int=Field(example=120)


class LivreCreateModel(LivreBaseModel):
    code_cat:str=Field(example="C0A1T2")

class LivreUpdateModel(LivreBaseModel):
    code_cat:str=Field(example="C0A1T2")

class LivrePatchModel(BaseModel):
    titre:Optional[str]=Field(default=None,example="Merlin l'enchanteur")
    contenue:Optional[str]=Field(default=None,example="Merlin l'enchanteur est un film de Walt Disney Pictures réalisé par Wolfgang Reitherman, sorti en 1963.")
    nbr_pages:Optional[int]=Field(default=None,example=120)
    code_cat:Optional[str]=Field(default=None,example="C0A1T2")


class LivrePydanticModel(LivreBaseModel):
    id:int
    categorie:"MetaCategorieModel"
    livres_ecritures : List["MetaEcritureModel"]=[]
    class Config:
        from_attributes=True


