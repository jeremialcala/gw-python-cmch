# -*- coding: utf-8 -*-
import json
import logging.config
import time
import asyncio

from starlette.concurrency import iterate_in_threadpool
from fastapi import FastAPI, Request, Response
from fastapi import status
from inspect import currentframe


from classes import Settings

app = FastAPI(
    title="Sistema de Control de Beneficios",
    version="1.0"
)
_set = Settings()

@app.get('/')
def mensaje():
    return 'Hola'

@app.post('/personas')
async def registrar_persona(request:Request):
    data=await request.json()
    return Response(status_code=200)

@app.put('/personas/{id_persona}')
async def update_persona(request:Request):
    return Response(status_code=200)

@app.delete('/personas/{id_persona}')
async def delete_persona(request:Request):
    return Response(status_code=200)