from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form

from bibliogest.livre.meta_models import MetaLivreModel

class CategorieBaseModel(BaseModel):
    nom : str = Field(example="Science-fiction")

class CategorieCreateModel(CategorieBaseModel):
    pass

class CategorieUpdateModel(CategorieBaseModel):
    pass

class CategoriePatchModel(BaseModel):
    nom : Optional[str] = Field(None, example="Science-fiction")

class CategoriePydanticModel(CategorieBaseModel):
    code : str
    livres: List["MetaLivreModel"] = []
    class Config:
        from_attributes=True


