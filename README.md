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

[Página oficial de FastAPI](https://fastapi.tiangolo.com/)

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

## Desarmando el framework

### Path Operations

Path = Route = Endpoint

Operation = Método HTTP

1. GET ->  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.
2. HEAD -> pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.
3. POST -> se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.
4. PUT -> reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.
5. DELETE -> borra un recurso en específico.
6. CONNECT -> establece un túnel hacia el servidor identificado por el recurso.
7. OPTIONS -> es utilizado para describir las opciones de comunicación para el recurso de destino.
8. TRACE -> realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.
9. PATCH -> es utilizado para aplicar modificaciones parciales a un recurso.

[Documentación de Developer Mozilla](https://developer.mozilla.org/es/docs/Web/HTTP/Methods)

### Path Parameters

Podemos crear variables dentro de los endpoints, se les llama **Path Parameters**. Si yo los defino, entonces es obligatorio usarlos. Por ejemplo: `/tweets/{tweet_id}`.

### Query Parameters

User -> método PUT => `/users/{user_id}/details?age=20&name=Juan`

Usando los '?' usamos los query parameters y con el '&' usamos varios al mismo tiempo.

### Request Body y Response Body

- Request body en FastAPI es el body de una petición HTTP.
- Response body en FastAPI es el body de una respuesta HTTP.

### Models

Esto va de la mano con las Bases de Datos. Piensa en los modelos como entidades. Un modelo es la descripción en código de una entidad de la vida real. Como una persona, casa, animal, etc.

Necesitamos usar a Pydantic y a Base Model para crear los modelos.

En FastAPI, el `...` quiere decir que es un parámetro obligatorio.

## Validaciones

### Validaciones: Query Parameters

En este ejemplo estamos haciendo que un query parameter sea obligatorio, lo cual no es ni muy común ni buena práctica, pero es para fines didácticos.

```python
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return {"name": name, "age": age}

```

Con esto, si accedemos  `http://localhost:8000/person/detail?name=Miguel&age=23` obtenemos un JSON:

```json
{
  "name": "Miguel",
  "age": 23
}
```

### Validaciones: explorando más parameters

- ge -> greater or equal than `>=`
- le -> less or equal than `<=`
- gt -> greater than `>`
- lt -> less than `<`

### Validaciones: Path Parameters

```python

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

```

### Validaciones: Request Body

Creamos una nueva clase:

```python
class Location(BaseModel):
    city: str
    state: str
    country: str

```

Creamos un nuevo endpoint:

```python
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

```

Al enviar los valores, obtenemos por ejemplo este JSON:

```json
{
  "person:": {
    "first_name": "Miguel",
    "last_name": "Reyes",
    "age": 23,
    "hair_color": "brown",
    "is_married": false
  },
  "person_id": 1,
  "location": {
    "city": "Piedras Negras",
    "state": "Coahuila",
    "country": "México"
  }
}
```

### Validaciones: Models

Importamos más paquetes y actualizamos el código:

```python
#Python
from typing import Optional
from enum import Enum #Podemos crear enumaraciones de Strings

#Pydantic
from pydantic import BaseModel
from pydantic import Field # Es lo mismo que Body, Query, Path

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


class HairColor(Enum):
    RED = "red"
    BLONDE = "blonde"
    BROWN = "brown"
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"


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

```

Ahora tenemos validaciones en los modelos y solo tenemos ciertos valores permitidos para los campos.

### Tipos de datos especiales

- Clásicos
  - String
  - Int
  - float
  - double
  - boolean
- Exóticos
  - Enum -> Para datos específicos
  - HttpUrl -> Para urls `https://www.google.com`
  - FilePath -> Para validar rutas de archivos `c:/windows/system32/algo.dll`
  - DirectoryPath -> Para validar ruta de directorios `/mnt/c/somefolder`
  - EmailString -> Para validar emails `hola@ejemplo.com`
  - PaymentCardNumber -> Para validar tarjetas de crédito/débito `454545XXXXXXXXXX`
  - IPvAnyAddress -> Para validar direcciones IP `127.0.0.1`
  - NegativeFloat -> Para validar números decimales negativos
  - PositiveFloat
  - NegativeInt
  - PositiveInt

[Documentación de Pydantic para tipos de datos](https://pydantic-docs.helpmanual.io/usage/types/#pydantic-types)

Actualiación de código:

```python
#Python
from typing import Optional
from enum import Enum #Podemos crear enumaraciones de Strings

#Pydantic
from pydantic import BaseModel
from pydantic import Field # Es lo mismo que Body, Query, Path
from pydantic import EmailStr
from pydantic import PaymentCardNumber
from pydantic.color import Color

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
    city: str = Field(
        ...,
        min_length=1,
        max_length=75
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=75
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=75
    )


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
    email: EmailStr = Field(
        ...,
        title="Email",
        description="Email of the person. Must be valid.",
    )
    payment_card_number: PaymentCardNumber = Field(
        ...,
        title="Payment card number",
        description="Payment card number of the person to pay our services. Must be valid.",
    )
    favorite_color: Optional[Color] = Field(default=None)



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
        title="Person name.",
        description="This is the person name. It's between 1 and 50 characters.",
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
        title="Person ID.",
        description="This is the person ID. It's required and must be greater than 0.",
        )
):
    return {"person_id": person_id}


# Validations: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID.",
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

```

## Ejemplos

### Creando ejemplos de Request Body automáticos

Podemos poner valores por defecto los body parameters. Debemos crear una clase dentro de nuestra clase.

```python
class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=75
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=75
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=75
    )

    class Config:
        schema_extra = {
            "example": {
                "city": "Los Angeles",
                "state": "California",
                "country": "USA"
            }
        }


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
    hair_color: Optional[HairColor] = Field(default=None, example="brown")
    is_married: Optional[bool] = Field(default=None, example=False)
    email: EmailStr = Field(
        ...,
        title="Email",
        description="Email of the person. Must be valid."
    )
    payment_card_number: PaymentCardNumber = Field(
        ...,
        title="Payment card number",
        description="Payment card number of the person to pay our services. Must be valid."
    )
    favorite_color: Optional[Color] = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Miguel",
                "last_name": "Reyes",
                "age": 23,
                "hair_color": "brown",
                "is_married": False,
                "email": "miguel@gmail.com",
                "payment_card_number": "5428614385158093"
            }
        }

```

Y tendremos un JSON con valores por defecto:

```json
{
  "person": {
    "first_name": "Miguel",
    "last_name": "Reyes",
    "age": 23,
    "hair_color": "brown",
    "is_married": false,
    "email": "miguel@gmail.com",
    "payment_card_number": "5428614385158093"
  },
  "location": {
    "city": "Los Angeles",
    "state": "California",
    "country": "USA"
  }
}
```

### Creando ejemplos de Path y Query parameters automáticos
