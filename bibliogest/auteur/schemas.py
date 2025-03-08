from pydantic import BaseModel, Field
from typing import List, Optional
from bibliogest.ecriture.meta_models import MetaLivreEcritureModel

class AuteurBaseModel(BaseModel):
    nom :str = Field(example="Harlequelrah")
    prenom : str =Field(example="Elrah")

class AuteurCreateModel(AuteurBaseModel):
    pass

class AuteurUpdateModel(AuteurBaseModel):
    pass

class AuteurPatchModel(BaseModel):
    nom : Optional[str] = Field(default=None, example="Harlequelrah")
    prenom : Optional[str] = Field(default=None, example="Elrah")

class AuteurPydanticModel(AuteurBaseModel):
    id : int
    auteur_ecritures : List[Optional["MetaLivreEcritureModel"]] = []
    class Config:
        from_attributes=True

