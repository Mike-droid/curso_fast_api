#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body


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
