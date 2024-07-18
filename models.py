from typing import Optional, List
from pydantic import BaseModel, Field

class WhoisResponse(BaseModel):
    domain_name: str
    registrant_id: Optional[str] = Field(default="Отсутствует")
    registrant_name: Optional[str] = Field(default="Отсутствует")
    organization: Optional[str] = Field(default="Отсутствует")
    address: Optional[str] = Field(default="Отсутствует")
    city: Optional[str] = Field(default="Отсутствует")
    region: Optional[str] = Field(default="Отсутствует")
    country: Optional[str] = Field(default="Отсутствует")
    phone: Optional[str] = Field(default="Отсутствует")
    email: Optional[str] = Field(default="Отсутствует")
    status: List[str] = Field(default_factory=list)
    registrar: Optional[str] = Field(default="Отсутствует")
    nameservers: List[str] = Field(default_factory=list)
    expiration_date: Optional[str] = Field(default="Отсутствует")