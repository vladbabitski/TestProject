import logging
from typing import List
from pydantic import BaseModel, ValidationError, RootModel


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class Model(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class ItemList(RootModel):
    root: List[Model]


def validate_api_response(response_data):
    data = response_data.json()
    try:
        ItemList.model_validate(data)
    except ValidationError as e:
        logging.info(f"After result validation an error has been occurred: {e}")
    else:
        logging.info("Data is valid")
