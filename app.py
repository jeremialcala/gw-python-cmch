# -*- coding: utf-8 -*-
import json
import logging.config
import time
import asyncio

from inspect import currentframe
from starlette.concurrency import iterate_in_threadpool
from fastapi import FastAPI, Request, Response
from fastapi import status
from fastapi.encoders import jsonable_encoder

from classes import Persona, Nomina, Unidad, Beneficio, Producto, Usuario
from classes import Settings
from utils import configure_logging

_set = Settings()
logging.config.dictConfig(configure_logging())
log = logging.getLogger(_set.environment)

app = FastAPI(
    title="Sistema de Control de Beneficios (SCB)",
    version="1.0",
    on_startup=[configure_logging],
)

_set = Settings()

@app.post('/personas', tags=['personas'])
async def registrar_persona(persona: Persona):
    log.info(f"Starting: {currentframe().f_code.co_name}")
    log.info(f"This is a new request {request.client}")
    data = jsonable_encoder(persona)

    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/personas/{cedula}', tags=['personas'])
async def consultar_persona(cedula:int):
    log.info(f"Starting: {currentframe().f_code.co_name}")    
    return Response(status_code=200)


@app.put('/personas/{id_persona}', tags=['personas'])
async def actualizar_persona(id_persona: int, persona: Persona):
    data = jsonable_encoder(persona)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/personas/{id_persona}', tags=['personas'])
async def eliminar_persona(id_persona: int):
    return Response(status_code=200)


@app.post('/nomina', tags=['nominas'])
async def registrar_nomina(nomina: Nomina):
    data = jsonable_encoder(nomina)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/nominas/{codnom}', tags=['nominas'])
async def consultar_nomina(codnom: int):
    return Response(status_code=200)


@app.put('/nominas/{codnom}', tags=['nominas'])
async def actualizar_nomina(codnom: int, nomina: Nomina):
    data = jsonable_encoder(nomina)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/nominas/{codnom}', tags=['nominas'])
async def eliminar_nomina(codnom:int):
    return Response(status_code=200)

@app.post('/unidades', tags=['unidades'])
async def registrar_unidad(unidad: Unidad):
    data = jsonable_encoder(unidad)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/unidades/{id_und}', tags=['unidades'])
async def consultar_unidad(id_und: int):
    pass


@app.put('/unidades/{id_und}', tags=['unidades'])
async def actualizar_unidad(id_und: int, unidad:Nomina):
    data = jsonable_encoder(unidad)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/unidades/{id_und}', tags=['unidades'])
async def eliminar_unidad(id_und: int):
    pass


@app.post('/productos', tags=['productos'])
async def registrar_producto(producto: Producto):
    data = jsonable_encoder(producto)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/productos/{id_producto}', tags=['productos'])
async def consultar_producto(id_producto: int):
    return Response(status_code=200)


@app.put('/productos/{id_producto}', tags=['productos'])
async def actualizar_unidad(id_producto: int, producto: Producto):
    data = jsonable_encoder(producto)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/productos/{id_producto}', tags=['productos'])
async def eliminar_producto(id_producto: int):
    return Response(status_code=200)



@app.post('/beneficios', tags=['beneficios'])
async def registrar_beneficio(benefico: Beneficio):
    data = jsonable_encoder(benefico)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/beneficios/{id_beneficio}', tags=['beneficios'])
async def consultar_beneficio(id_beneficio: int):
    return Response(status_code=200)


@app.put('/beneficios/{id_beneficio}', tags=['beneficios'])
async def actualizar_benefcio(id_beneficio: int, beneficio: Beneficio):
    data = jsonable_encoder(beneficio)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/beneficios/{id_beneficio}', tags=['beneficios'])
async def eliminar_beneficio(id_beneficio: int):
    return Response(status_code=200)


@app.post('/seguridad', tags=['seguridad'])
async def registrar_usuaro(usuario: Usuario):
    data = jsonable_encoder(usuario)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/seguridad/{user}', tags=['seguridad'])
async def consultar_usuario(user: str):
    return Response(status_code=200)


@app.put('/seguridad/{user}', tags=['seguridad'])
async def restablecer_clave(user: str):
    return Response(status_code=200)


@app.delete('/seguridad/{id_user}', tags=['seguridad'])
async def eliminar_usuario(id_usuario: int):
    return Response(status_code=200)
