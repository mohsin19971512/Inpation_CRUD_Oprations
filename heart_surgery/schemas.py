from ninja import ModelSchema, Schema
from ninja.orm import create_schema
from pydantic import UUID4
from typing import List




class ProfileSchemaOut(Schema):
    name : str 
    age : str 
    weight :  str 
    gender : str
    number : str
    Ward : str
    Bed : str
