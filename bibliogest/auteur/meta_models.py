
from pydantic import BaseModel, Field


class MetaAuteurModel(BaseModel):
    id:int
    nom :str = Field(example="Harlequelrah")
    prenom : str =Field(example="Elrah")
