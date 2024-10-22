from pydantic import BaseModel, Field
from datetime import date

class Persona(BaseModel):
    id_persona: int = Field(gt=0)
    cedula: int = Field(gt=99999, lt=100000000)
    nombre: str = Field(min_length=7, max_length=15)
    apellido: str = Field(min_length=7, max_length=40)
    estatus: int = Field(gt=0)
    fecha_nac: date
    fecha_ingreso: date

class Nomina(BaseModel):
    id_nomina: int = Field(min_length=1)
    codnom: int = Field(defalt="001", min_length=3,max_length=3)
    descripcion: str = Field(default="Nómina de", min_length= 10, max_length=50)
    estatus: int = Field(min_length=1)

class Unidad(BaseModel):
    id_unidad: int = Field(min_length=1)
    descripcion: str = Field(default="Nómina de", min_length= 10, max_length=50)
    estatus: int = Field(min_length=1)

class Producto(BaseModel):
    id_producto: int = Field(min_length=1)
    descripcion: str = Field(default="Nómina de", min_length= 10, max_length=50)
    estatus: int = Field(min_length=1)

class Beneficio(BaseModel):
    id_beneficio: int = Field(min_length=1)
    fecha_entrega: date
    tipo_benefico: int = Field(min_length=1)
    estatus: int = Field(min_length=1)

class Usuario(BaseModel):
    id_usuario: int = Field(min_length=1)
    username: str = Field(min_length= 5, max_length=10)
    password: str = Field(min_length= 5, max_length=10)
    fecha_registro: date
    estatus: int = Field(min_length=1)