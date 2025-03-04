from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form


class CategorieBaseModel(BaseModel):
    pass

class CategorieCreateModel(BaseModel):
    pass

class CategorieUpdateModel(BaseModel):
    pass

class CategoriePatchModel(BaseModel):
    pass

class CategoriePydanticModel(BaseModel):
    pass
