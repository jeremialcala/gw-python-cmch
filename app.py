# -*- coding: utf-8 -*-
import json
import logging.config
import time
import asyncio

from starlette.concurrency import iterate_in_threadpool
from fastapi import FastAPI, Request, Response
from fastapi import status
from inspect import currentframe
from fastapi.encoders import jsonable_encoder

from dto import Persona
from dto import Nomina
from dto import Unidad
from dto import Beneficio

from dto import Producto
from dto import Usuario
from classes import Settings

app = FastAPI(
    title="Sistema de Control de Beneficios (SCB)",
    version="1.0"
)
_set = Settings()


@app.post('/personas', tags=['personas'])
async def registrar_persona(persona: Persona):
    data = persona
    Persona.append(jsonable_encoder(data))
    return Persona

@app.get('/personas/{cedula}', tags=['personas'])
async def consultar_persona(cedula:int):
    return Response(status_code=200)
    pass

@app.put('/personas/{id_persona}', tags=['personas'])
async def actualizar_persona(id_persona: int):
    return Response(status_code=200)
    pass

@app.delete('/personas/{id_persona}', tags=['personas'])
async def eliminar_persona(id_persona: int):
    return Response(status_code=200)
    pass



@app.post('/nomina', tags=['nominas'])
async def registrar_nomina(nomina: Nomina):
    return Response(status_code=200)
    pass

@app.get('/nominas/{codnom}', tags=['nominas'])
async def consultar_nomina(codnom: int):
    return Response(status_code=200)

@app.put('/nominas/{codnom}', tags=['nominas'])
async def actualizar_nomina(codnom: int):
    return Response(status_code=200)

@app.delete('/nominas/{codnom}', tags=['nominas'])
async def eliminar_nomina(codnom:int):
    return Response(status_code=200)




@app.post('/unidades', tags=['unidades'])
async def registrar_unidad(unidad: Unidad):
    return Response(status_code=200)

@app.get('/unidades/{id_und}', tags=['unidades'])
async def consultar_unidad(id_und: int):
    pass

@app.put('/unidades/{id_und}', tags=['unidades'])
async def actualizar_unidad(id_und: int):
    pass

@app.delete('/unidades/{id_und}', tags=['unidades'])
async def eliminar_unidad(id_und: int):
    pass



@app.post('/productos', tags=['productos'])
async def registrar_producto(producto: Producto):
    return Response(status_code=200)

@app.get('/productos/{id_producto}', tags=['productos'])
async def consultar_producto(id_producto: int):
    return Response(status_code=200)

@app.put('/productos/{id_producto}', tags=['productos'])
async def actualizar_unidad(id_producto: int):
    return Response(status_code=200)

@app.delete('/productos/{id_producto}', tags=['productos'])
async def eliminar_producto(id_producto: int):
    return Response(status_code=200)




@app.post('/beneficios', tags=['beneficios'])
async def registrar_beneficio(benefico: Beneficio):
    return Response(status_code=200)

@app.get('/beneficios/{id_beneficio}', tags=['beneficios'])
async def consultar_beneficio(id_beneficio: int):
    return Response(status_code=200)

@app.put('/beneficios/{id_beneficio}', tags=['beneficios'])
async def actualizar_benefcio(id_beneficio: int):
    return Response(status_code=200)

@app.delete('/beneficios/{id_beneficio}', tags=['beneficios'])
async def eliminar_beneficio(id_beneficio: int):
    return Response(status_code=200)





@app.post('/seguridad', tags=['seguridad'])
async def registrar_usuaro(usuario: Usuario):
    return Response(status_code=200)

@app.get('/seguridad/{user}', tags=['seguridad'])
async def consultar_usuario(user: str):
    return Response(status_code=200)

@app.put('/seguridad/{user}', tags=['seguridad'])
async def restablecer_clave(user: str):
    return Response(status_code=200)

@app.delete('/seguridad/{id_user}', tags=['seguridad'])
async def eliminar_usuario(id_usuario: int):
    return Response(status_code=200)




@app.post('/personas', tags=['otros'])
async def registrar_persona(request:Request):
    """
    
    """
    data=await request.json()
    return Response(status_code=200)