from bibliogest.categorie.models import Categorie
from bibliogest.categorie.schemas import CategorieCreateModel, CategorieUpdateModel,CategoriePatchModel
from elrahapi.crud.crud_forgery import CrudForgery
from bibliogest.settings.database import authentication

categorie_crud = CrudForgery(
    entity_name="categorie",
    primary_key_name="code",
    authentication=authentication,
    SQLAlchemyModel=Categorie,
    CreatePydanticModel=CategorieCreateModel,
    UpdatePydanticModel=CategorieUpdateModel,
    PatchPydanticModel=CategoriePatchModel
)
