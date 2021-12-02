# Curso de FastAPI: Fundamentos, Path Operations y Validaciones

## Introducción

### ¿Qué necesitas para aprender FastAPI?

- Python básico
- Git y Github
- POO
- Python Profesional
- Introducción al desarrollo backend

## Fundamentos de FastAPI

### ¿Qué es FastAPI?

FastAPI es un framework para crear APIs con Python. Es de los más rápidos que existen, compite contra Node.js y Go. Esta tecnología fue creada por [Sebastián Ramírez](https://twitter.com/tiangolo).

Fast API es usado por Uber, Windows, Netflix. y Office.

### Ubicación de FastAPI en el ecosistema de Python

FastAPI tiene bases en [uvicorn](https://www.uvicorn.org/), [Starlette](https://www.starlette.io/) y [Pydantic](https://pydantic-docs.helpmanual.io/).

- Uvicorn: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor
- Starlette: es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente
- Pydantic: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API

### Hello World: creación del entorno de desarrollo

Debemos crear un entorno virtual en Python y cuando se esté ejecutando, instalamos `pip install fastapi uvicorn`.

Creamos un archivo main.py:

```python
from fastapi import FastAPI

app = FastAPI() # Todo nuestro programa se carga en la variable

@app.get("/")
def home():
    return {"message": "Hello World"}
```

Ejecutamos desde la terminal: `uvicorn main:app --reload` Este parámetro es un hot reload.

### Documentación interactiva de una API

FastAPI funciona sobre, también, OpeanAPI. Es un conjunto de reglas que permite definir algo, en este caso, como describir APIs.

Pero necesitamos usar Swagger o ReDoc.

Si ingresas a 'https://localhost:8000/docs' verás que ya tienes la documentación creada con Swagger.

Si ingresas a 'https://localhost:8000/redoc' verás que ya tienes la documentación creada con ReDoc.
