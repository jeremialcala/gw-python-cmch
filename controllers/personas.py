
import logging.config

from inspect import currentframe

from .amqp import send_message_to_queue
from classes import Settings, Persona
from utils import configure_logging

_set = Settings()
logging.config.dictConfig(configure_logging())
log = logging.getLogger(_set.environment)

async def ctr_crear_persona(persona: Persona):
    pass

async def ctr_buscar_persona(persona_id: str):
    pass