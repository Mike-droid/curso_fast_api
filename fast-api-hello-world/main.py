#Python
from typing import Optional
from enum import Enum #Podemos crear enumaraciones de Strings

#Pydantic
from pydantic import BaseModel
from pydantic import Field # Es lo mismo que Body, Query, Path

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI() # Todo nuestro programa se carga en la variable


# Models

class HairColor(Enum):
    RED = "red"
    BLONDE = "blonde"
    BROWN = "brown"
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"


class Location(BaseModel):
    city: str
    state: str
    country: str


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str= Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


@app.get("/") #path operation decorator
def home(): #path operation function
    return {"message": "Hello World, I'm using Python and FastAPI 🐍"}


# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)): # Los '...' indican que es obligatorio
    return person


# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is the person name. It's between 1 and 50 characters",
        ),
    age: int = Query(
        ...,
        title="Person age",
        description="This is the person age. It's required",
        )
):
    return {"name": name, "age": age}


# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's required and must be greater than 0",
        )
):
    return {"person_id": person_id}


# Validations: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID.",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...),
):
    return {
        "person_id": person_id,
        "person:": person,
        "location": location,
    }
