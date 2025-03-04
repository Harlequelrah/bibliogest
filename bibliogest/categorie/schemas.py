from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form

class CategorieBaseModel(BaseModel):
    nom : str = Field(example="Science-fiction")

class CategorieCreateModel(CategorieBaseModel):
    pass

class CategorieUpdateModel(CategorieBaseModel):
    pass

class CategoriePatchModel(BaseModel):
    nom : Optional[str] = Field(None, example="Science-fiction")

class CategoriePydanticModel(BaseModel):
    code : str
    livres: List["MetaLivre"] = []

class MetaCategorieModel(BaseModel):
    code : str
    nom : str
