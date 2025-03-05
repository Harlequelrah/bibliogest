from bibliogest.auteur.models import SQLAlchemyModel
from bibliogest.auteur.schemas import AuteurCreateModel, AuteurUpdateModel,AuteurPatchModel
from elrahapi.crud.crud_forgery import CrudForgery
from bibliogest.settings.database import authentication

auteur_crud = CrudForgery(
    entity_name="auteur",
    primary_key_name="id",
    authentication=authentication,
    SQLAlchemyModel=SQLAlchemyModel,
    CreatePydanticModel=AuteurCreateModel,
    UpdatePydanticModel=AuteurUpdateModel,
    PatchPydanticModel=AuteurPatchModel,


)
