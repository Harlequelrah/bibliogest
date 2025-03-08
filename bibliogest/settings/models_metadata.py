from .database import Base
from bibliogest.livre.models import metadata as myapp_metadata1
from bibliogest.categorie.models import metadata as myapp_metadata2
from bibliogest.ecriture.models import metadata as myapp_metadata3
from bibliogest.auteur.models import metadata as myapp_metadata4
from bibliogest.loggerapp.log_model import metadata as myapp_metadata5
from bibliogest.userapp.user_models import metadata as myapp_metadata6
from sqlalchemy import MetaData

target_metadata = MetaData()

target_metadata = Base.metadata
target_metadata = myapp_metadata1
target_metadata = myapp_metadata2
target_metadata = myapp_metadata3
target_metadata = myapp_metadata4
target_metadata = myapp_metadata5
target_metadata = myapp_metadata6


