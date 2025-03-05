

from pydantic import BaseModel

from bibliogest.auteur.meta_models import MetaAuteurModel
from bibliogest.livre.meta_models import MetaLivreModel



class MetaEcritureModel(BaseModel):
    auteur : "MetaAuteurModel"
    livre : "MetaLivreModel"
