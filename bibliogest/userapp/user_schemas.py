from elrahapi.user import  model
from bibliogest.settings import authentication
class UserBaseModel(model.UserBaseModel):
    pass

class UserCreateModel(model.UserCreateModel):
    pass

class UserUpdateModel(model.UserUpdateModel):
    pass

class UserPatchModel(model.UserPatchModel):
    pass

class UserReadModel(UserBaseModel):
    class Config :
        from_attributes=True

authentication.UserReadModel = UserReadModel
authentication.UserCreateModel = UserCreateModel
authentication.UserUpdateModel = UserUpdateModel
authentication.UserPatchModel = UserPatchModel


