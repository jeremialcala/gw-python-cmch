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
from classes import Persona, Nomina, Unidad, Beneficio, Producto, Usuario

#from classes import Settings
import aio_pika
import logging
log=logging.getLogger()

app = FastAPI(
    title="Sistema de Control de Beneficios (SCB)",
    version="1.0"
)

#_set = Settings()

# Function to send message to RabbitMQ
async def send_message(message: dict):
#    log.info(f"test: {message}")
    try:
        connection = await aio_pika.connect_robust("amqp://soportecmch:s0p0rt3cmch@172.16.10.147:30672/")
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue("ENVIO_DE_MENSAJES", durable=True)
            await channel.default_exchange.publish(
                aio_pika.Message(body=json.dumps(message).encode()),
                routing_key=queue.name
            )
            log.info("Message sent to RabbitMQ")
    except Exception as e:
        log.error(f"Failed to send message: {e}")

# Function to receive messages from RabbitMQ
async def receive_messages():
    connection = await aio_pika.connect_robust("amqp://soportecmch:s0p0rt3cmch@172.16.10.147:30672/")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("RECEPCION_MENSAJES", durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(f"Received message: {message.body.decode()}")

@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(receive_messages())

@app.post('/personas', tags=['personas'])
async def registrar_persona(persona: Persona):
    data = jsonable_encoder(persona)
    await send_message(data)  
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/personas/{cedula}', tags=['personas'])
async def consultar_persona(cedula:int):
    return Response(status_code=200)
    pass


@app.put('/personas/{id_persona}', tags=['personas'])
async def actualizar_persona(id_persona: int, persona: Persona):
    data = jsonable_encoder(persona)
    await send_message(data)  # Send data to RabbitMQ
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.delete('/personas/{id_persona}', tags=['personas'])
async def eliminar_persona(id_persona: int):
    return Response(status_code=200)
    pass



@app.post('/nomina', tags=['nominas'])
async def registrar_nomina(nomina: Nomina):
    data = jsonable_encoder(nomina)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/nominas/{codnom}', tags=['nominas'])
async def consultar_nomina(codnom: int):
    return Response(status_code=200)

@app.put('/nominas/{codnom}', tags=['nominas'])
async def actualizar_nomina(codnom: int, nomina: Nomina):
    data = jsonable_encoder(nomina)
    await send_message(data)  
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/nominas/{codnom}', tags=['nominas'])
async def eliminar_nomina(codnom:int):
    return Response(status_code=200)

@app.post('/unidades', tags=['unidades'])
async def registrar_unidad(unidad: Unidad):
    data = jsonable_encoder(unidad)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/unidades/{id_und}', tags=['unidades'])
async def consultar_unidad(id_und: int):
    pass

@app.put('/unidades/{id_und}', tags=['unidades'])
async def actualizar_unidad(id_und: int, unidad:Nomina):
    data = jsonable_encoder(unidad)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/unidades/{id_und}', tags=['unidades'])
async def eliminar_unidad(id_und: int):
    pass



@app.post('/productos', tags=['productos'])
async def registrar_producto(producto: Producto):
    data = jsonable_encoder(producto)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.get('/productos/{id_producto}', tags=['productos'])
async def consultar_producto(id_producto: int):
    return Response(status_code=200)

@app.put('/productos/{id_producto}', tags=['productos'])
async def actualizar_unidad(id_producto: int, producto: Producto):
    data = jsonable_encoder(producto)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/productos/{id_producto}', tags=['productos'])
async def eliminar_producto(id_producto: int):
    return Response(status_code=200)




@app.post('/beneficios', tags=['beneficios'])
async def registrar_beneficio(benefico: Beneficio):
    data = jsonable_encoder(benefico)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/beneficios/{id_beneficio}', tags=['beneficios'])
async def consultar_beneficio(id_beneficio: int):
    return Response(status_code=200)

@app.put('/beneficios/{id_beneficio}', tags=['beneficios'])
async def actualizar_benefcio(id_beneficio: int, beneficio: Beneficio):
    data = jsonable_encoder(beneficio)
    await send_message(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})


@app.delete('/beneficios/{id_beneficio}', tags=['beneficios'])
async def eliminar_beneficio(id_beneficio: int):
    return Response(status_code=200)



@app.post('/seguridad', tags=['seguridad'])
async def registrar_usuaro(usuario: Usuario):
    data = jsonable_encoder(usuario)
    await send_message(data)  
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



