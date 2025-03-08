from bibliogest.livre.models import Livre
from bibliogest.livre.schemas import LivreCreateModel, LivreUpdateModel,LivrePatchModel
from elrahapi.crud.crud_forgery import CrudForgery
from bibliogest.settings.database import authentication

livre_crud = CrudForgery(
    entity_name="livre",
    primary_key_name="id",
    authentication=authentication,
    SQLAlchemyModel=Livre,
    CreatePydanticModel=LivreCreateModel,
    UpdatePydanticModel=LivreUpdateModel,
    PatchPydanticModel=LivrePatchModel
)
