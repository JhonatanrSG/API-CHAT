import os
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplaza "*" con la lista de orígenes permitidos.
    allow_methods=["*"],  # O reemplaza "*" con la lista de métodos permitidos (por ejemplo, ["GET", "POST"]).
    allow_headers=["*"],  # O reemplaza "*" con la lista de encabezados permitidos.
    allow_credentials=True,  # Habilita la inclusión de credenciales (cookies, encabezados de autorización, etc.).
    expose_headers=["*"],  # O reemplaza "*" con la lista de encabezados expuestos.
)


@app.get("/")
def root():
    return {
        "Service": "Integracion Back OpenIA"
    }


@app.post("/chat")
def chat(pregunta: dict):
    openai.api_key = "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"

    contexto = ("Te van a hacer preguntas sobre la base de datos AdventureWorks2019, son colsultas especificas a las que tu tienes acceso por medio de una conexion local a la base de datos, por favor intenta convertir la pregunta a la sentencia sql, solo responde con la sentencia sql")

    print(pregunta)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": contexto + pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content = response.choices[0].message.content

    return {

        "Respuesta": content
    }

##contexto = ("Tu nombre es Py-problem, por favor responde como un asistente virtual que resuelve problemas de programacion, si te preguntan de un tema diferente por favor di, solo respondo preguntas de ing de sistemas:")

