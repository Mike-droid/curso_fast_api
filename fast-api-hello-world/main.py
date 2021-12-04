from fastapi import FastAPI

app = FastAPI() # Todo nuestro programa se carga en la variable

@app.get("/") #path operation decorator
def home(): #path operation function
    return {"message": "Hello World, I'm using Python and FastAPI 🐍"}

