"""
    This controller is in charge of session operation
"""
import logging.config
import json
from uuid import uuid4
from inspect import currentframe

from .amqp import send_message_to_queue
from fastapi import Request, Response
from classes import Settings
from enums import Operations
from constants import STARTING_AT, ENDING_AT, CONTENT_TYPE, APPLICATION_JSON
from utils import (configure_logging, create_model,create_dynamic_dto_model, 
                   create_dynamic_orm_model, resource_from_model)
from classes import ResponseData

_set = Settings()
logging.config.dictConfig(configure_logging())
log = logging.getLogger(_set.environment)

# Here we are creating the generic objects
message = create_dynamic_dto_model("message", json.loads(_set.message))
session_dto = create_dynamic_dto_model("session_dto", json.loads(_set.session_dto))


async def ctr_create_session(request: Request):
    resp_body = ResponseData(code = 503, message= "Internal Server Error", )
    response = Response(
        content=resp_body.json(),
        status_code=resp_body.code,
        headers={CONTENT_TYPE: APPLICATION_JSON}
    )

    try:
        body = await request.json()
        session = session_dto(**body)

        _message = message(
            messageId=uuid4().__str__(), 
            resource="session", 
            origen=_set.service_name, 
            operation=Operations.POST, 
            destination="None", 
            body=session.__str__()
        )

        log.info(_message.json())
    except Exception as e:
        log.error(e.__str__())
    finally:
        return response
