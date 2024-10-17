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
    title="Sistema de Control de Beneficios (SCB)",
    version="1.0"
)
_set = Settings()

@app.post('/personas', tags=['personas'])

@app.get('/personas/{id_persona}', tags=['personas'])

@app.put('/personas/{id_persona}', tags=['personas'])
async def update_persona(request:Request):
    return Response(status_code=200)

@app.delete('/personas/{id_persona}', tags=['personas'])
async def delete_persona(request:Request):
    return Response(status_code=200)



@app.post('/nomina', tags=['nominas'])

@app.get('/nominas/{codnom}', tags=['nominas'])

@app.put('/nominas/{codnom}', tags=['nominas'])

@app.delete('/nominas/{codnom}', tags=['nominas'])





@app.post('/unidades', tags=['unidades'])

@app.get('/unidades/{id_und}', tags=['unidades'])

@app.put('/unidades/{id_und}', tags=['unidades'])

@app.delete('/unidades/{id_und}', tags=['unidades'])





@app.post('/productos', tags=['productos'])

@app.get('/productos/{id_producto}', tags=['productos'])

@app.put('/productos/{id_producto}', tags=['productos'])

@app.delete('/productos/{id_producto}', tags=['productos'])





@app.post('/beneficios', tags=['beneficios'])

@app.get('/beneficios/{id_producto}', tags=['beneficios'])

@app.put('/beneficios/{id_producto}', tags=['beneficios'])

@app.delete('/beneficios/{id_producto}', tags=['beneficios'])




@app.post('/seguridad', tags=['seguridad'])

@app.get('/seguridad/{user}', tags=['seguridad'])

@app.put('/seguridad/{user}', tags=['seguridad'])

@app.delete('/seguridad/{user}', tags=['seguridad'])





@app.post('/personas', tags=['otros'])
async def registrar_persona(request:Request):
    """
    
    """
    data=await request.json()
    return Response(status_code=200)

