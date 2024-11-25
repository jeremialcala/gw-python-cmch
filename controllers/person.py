"""
    This controller is in charge of person operation
"""
import logging.config
import json
from inspect import currentframe

from .amqp import send_message_to_queue
from fastapi import Request, Response
from classes import Settings
from enums import Operations
from constants import STARTING_AT, ENDING_AT
from utils import (configure_logging, create_model,create_dynamic_dto_model, 
                   create_dynamic_orm_model, resource_from_model)

_set = Settings()
logging.config.dictConfig(configure_logging())
log = logging.getLogger(_set.environment)

# Here we are creating the generic objects
message = create_dynamic_dto_model("message", json.loads(_set.message))
person_dto = create_dynamic_dto_model("person_dto", json.loads(_set.person_dto))

async def ctr_person(request: Request):
    log.info(STARTING_AT, currentframe().f_code.co_name)
    """
        The main Controller for this operation.

    """
    match request.method:
        case Operations.POST.value:
            log.info("This is a POST")
            pass
        
        case Operations.GET.value:
            log.info("This is a GET")
            pass
        
        case Operations.PUT.value:
            pass
        
        case Operations.PATCH.value:
            pass
        
        case Operations.DELETE.value:
            pass
        
        case _ :
            raise NotImplemented("This method is not implemented for this resource")
        
    log.info(ENDING_AT, currentframe().f_code.co_name)
