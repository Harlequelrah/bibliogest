from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from bibliogest.auteur.meta_models import MetaAuteurModel
from bibliogest.livre.meta_models import MetaLivreModel

class EcritureBaseModel(BaseModel):
    auteur_id: int = Field(example=1)
    livre_id:int = Field(example=2)

class EcritureCreateModel(EcritureBaseModel):
    pass

class EcritureUpdateModel(EcritureBaseModel):
    pass

class EcriturePatchModel(BaseModel):
    auteur_id: Optional[int] =Field(example=6,default= None)
    livre_id: Optional[int] = Field(example=6,default=None)

class EcriturePydanticModel(BaseModel):
    id : int
    auteur : "MetaAuteurModel"
    livre : "MetaLivreModel"
    class Config:
        from_attributes=True





