from pydantic import BaseModel, Field




class EntityBaseModel(BaseModel):
    titre:str=Field(example="Merlin l'enchanteur")
    contenue:str=Field(example="Merlin l'enchanteur est un film de Walt Disney Pictures réalisé par Wolfgang Reitherman, sorti en 1963.")
    nbr_pages:int=Field(example=120$

class EntityCreateModel(BaseModel):
    pass

class EntityUpdateModel(BaseModel):
    pass

class EntityPatchModel(BaseModel):
    pass

class EntityPydanticModel(BaseModel):
    pass

class MetaEntityModel(BaseModel):
    pass
