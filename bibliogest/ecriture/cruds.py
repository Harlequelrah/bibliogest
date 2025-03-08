from bibliogest.ecriture.models import Ecriture
from bibliogest.ecriture.schemas import EcritureCreateModel, EcritureUpdateModel,EcriturePatchModel
from elrahapi.crud.crud_forgery import CrudForgery
from bibliogest.settings.database import authentication

ecriture_crud = CrudForgery(
    entity_name="ecriture",
    primary_key_name="id",
    authentication=authentication,
    SQLAlchemyModel=Ecriture,
    CreatePydanticModel=EcritureCreateModel,
    UpdatePydanticModel=EcritureUpdateModel,
    PatchPydanticModel=EcriturePatchModel
)
