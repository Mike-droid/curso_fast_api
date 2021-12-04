#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI() # Todo nuestro programa se carga en la variable


# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None # None = null en base de datos
    is_married: Optional[bool] = None


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
