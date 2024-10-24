# -*- coding: utf-8 -*-
"""
    This controller manages the AMQP, serving as the RabbitMQ interface.

"""
import threading
import logging.config
import functools
from inspect import currentframe
import pika
from pika.channel import Channel

from classes import Settings
from utils import configure_logging
from constants import STARTING_AT, ENDING_AT



_set = Settings()
log = logging.getLogger(__name__)
logging.config.dictConfig(configure_logging())


def get_amqp_connection_parameters(host=_set.qms_server, port=_set.qms_port):
    """
    :return: pika Connection parameters for RabbitMQ.
    """
    log.info(STARTING_AT, currentframe().f_code.co_name)
    credentials = pika.credentials.PlainCredentials(username=_set.qms_user,
                                                    password=_set.qms_password)

    conn_parameters = pika.ConnectionParameters(host=host, port=port,
                                                credentials=credentials)
    log.info(ENDING_AT, currentframe().f_code.co_name)
    return conn_parameters


def send_message_to_queue(queue: str, routing_key: str, message,
                          connection_parameters=get_amqp_connection_parameters()) -> None:
    """
        this will send a Message to a queue

    """
    log.info(STARTING_AT, currentframe().f_code.co_name)
    connection = pika.BlockingConnection(connection_parameters)

    # BasicProperties(
    #   [
    #       'delivery_mode=1',
    #       "headers=
    #           {
    #               'x-client-id': '21d738de-37b3-11ef-b696-2ba58bd1086f',
    #               'x-message-id': '5b9b6a36-37b3-11ef-b236-475a3364da4d'
    #           }"
    #   ]
    # ) >

    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange=_set.amqp_exchange,
                          routing_key=routing_key,
                          body=message)
    connection.close()
    log.info(ENDING_AT, currentframe().f_code.co_name)