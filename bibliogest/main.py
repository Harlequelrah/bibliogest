from fastapi import FastAPI
from bibliogest.settings.database import engine, authentication
from bibliogest.settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from bibliogest.auteur.router import app_auteur
from bibliogest.categorie.router import app_categorie
from bibliogest.livre.router import app_livre
from bibliogest.ecriture.router import app_ecriture
from bibliogest.loggerapp.log_router import app_logger
from bibliogest.loggerapp.log_model import Logger

from elrahapi.middleware.log_middleware import LoggerMiddleware
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_auteur)
app.include_router(app_categorie)
app.include_router(app_livre)
app.include_router(app_ecriture)
app.include_router(app_logger)
app.add_middleware(
    ErrorHandlingMiddleware,
    LoggerMiddlewareModel=Logger,
    session_factory=authentication.session_factory
)
app.add_middleware(
    LoggerMiddleware,
    LoggerMiddlewareModel=Logger,
    session_factory=authentication.session_factory
)

