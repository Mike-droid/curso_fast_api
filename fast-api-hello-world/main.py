from fastapi import FastAPI

app = FastAPI() # Todo nuestro programa se carga en la variable

@app.get("/")
def home():
    return {"message": "Hello World, I'm using Python and FastAPI 🐍"}

