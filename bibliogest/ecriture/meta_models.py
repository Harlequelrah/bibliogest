

from pydantic import BaseModel

from bibliogest.auteur.meta_models import MetaAuteurModel
from bibliogest.livre.meta_models import MetaLivreModel


class MetaAuteurEcritureModel(BaseModel):
    auteur:"MetaAuteurModel"

class MetaLivreEcritureModel(BaseModel):
    livre:"MetaLivreModel"
class MetaEcritureModel(MetaAuteurEcritureModel,MetaLivreEcritureModel):
    pass


