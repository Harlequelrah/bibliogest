
from pydantic import BaseModel


class MetaCategorieModel(BaseModel):
    code : str
    nom : str
