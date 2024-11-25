"""
    This is a Pydantic Settings file, we use it for config files and some other variables.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
        Each variable of this class represents a variable on a file config.env
    """

    service_name: str
    environment: str
    version: str

    db_name: str
    db_host: str
    db_username: str
    db_password: str

    amqp_host: str
    amqp_port: str
    amqp_user: str
    amqp_password: str

    amqp_exchange: str
    amqp_routing_key: str

    key_size: int
    private_key_filename: str
    public_key_filename: str

    message: str
    person_dto: str
    session_dto: str 
    
    model_config = SettingsConfigDict(env_file=".env")