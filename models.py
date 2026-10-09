from pydantic import BaseModel,EmailStr,Field
class RegisterRequest(BaseModel):
    name:str=Field(min_length=2,max_length=80); email:EmailStr; password:str=Field(min_length=6,max_length=128)
class LoginRequest(BaseModel):
    email:EmailStr; password:str=Field(min_length=1,max_length=128)
class HomeRequest(BaseModel):
    budget:float=Field(gt=0,le=10_000_000); rooms:list[str]=Field(min_length=1,max_length=8); style:str=Field(default='Modern',min_length=2,max_length=60); notes:str=Field(default='',max_length=500)
class PartyRequest(BaseModel):
    budget:float=Field(gt=0,le=10_000_000); guests:int=Field(gt=0,le=10_000); event_type:str=Field(min_length=2,max_length=60); venue:str=Field(default='Home / flexible',max_length=100); city:str=Field(default='Chennai',max_length=80); notes:str=Field(default='',max_length=500)
class JewelryRequest(BaseModel):
    budget:float=Field(gt=0,le=10_000_000); occasion:str=Field(min_length=2,max_length=80); style:str=Field(default='Elegant',max_length=80); metal:str=Field(default='Any',max_length=40); notes:str=Field(default='',max_length=500)
