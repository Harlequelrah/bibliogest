from elrahapi.router.route_config import  RouteConfig
from elrahapi.router.router_default_routes_name import DefaultRoutesName
from bibliogest.settings.database import authentication
from bibliogest.ecriture.cruds import ecriture_crud
from bibliogest.ecriture.schemas import EcriturePydanticModel
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/ecritures",
    tags=["ecriture"],
    PydanticModel=EcriturePydanticModel,
    crud=ecriture_crud
)

# app_ecriture = router_provider.get_public_router()
# app_ecriture = router_provider.get_protected_router()

init_data: List[RouteConfig] = [
    RouteConfig(route_name=DefaultRoutesName.CREATE, is_activated=True),
    RouteConfig(route_name=DefaultRoutesName.READ_ONE, is_activated=True),
    RouteConfig(route_name=DefaultRoutesName.READ_ALL, is_activated=True),
    RouteConfig(route_name=DefaultRoutesName.UPDATE, is_activated=True, is_protected=True),
    RouteConfig(route_name=DefaultRoutesName.DELETE, is_activated=True, is_protected=True),
]
app_ecriture = router_provider.initialize_router(init_data=init_data)
