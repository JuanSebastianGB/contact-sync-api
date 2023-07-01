from pydantic import BaseModel, EmailStr, constr
from datetime import datetime


class ApiCallSchema(BaseModel):
    timestamp: datetime
    endpoint: str
    params: str
    result: str


class ContactCreateSchema(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    phone: constr(regex=r'\(\d{3}\) \d{3}-\d{4}')
    website: str
