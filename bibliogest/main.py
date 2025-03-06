from fastapi import FastAPI
from bibliogest.settings.database import engine, authentication
from bibliogest.settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from bibliogest.auteur.router import app_auteur

app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_auteur)
app.add_middleware(
    ErrorHandlingMiddleware,
)

