from ninja import ModelSchema, Schema
from ninja.orm import create_schema
from pydantic import UUID4
from typing import List
import datetime

class MessageOut(Schema):
    message: str



class ProfileSchemaIn(Schema):
    name : str 
    age : str 
    weight :  str 
    gender : str
    number : str
    Ward : str
    Bed : str
    diagnoses : str
    operation_type : str
    entry_date_time :datetime.datetime
    operation_date_time :datetime.datetime
    leaving_date_time :datetime.datetime
    medications :str
    operative_finding :str
    operative_procedure :str
    operative_note :str
    specimen_to_laboratory :bool
    consultant_surgeon :str
    co_surgeon :str
    surgeon :str
    anesthetist :str
    nurse :str 
    sponge_nurse :str
    doctor_name:str

class ProfileNameSchemaOut(Schema):
    pk:UUID4= None
    name : str 

class ProfileSchemaOut(Schema):
    id : UUID4
    name : str 
    age : str 
    weight :  str 
    gender : str
    number : str 
    Ward : str
    Bed : str
    diagnoses : str
    operation_type : str
    entry_date_time :datetime.datetime
    operation_date_time :datetime.datetime
    leaving_date_time :datetime.datetime
    medications :str
    operative_finding :str
    operative_procedure :str
    operative_note :str
    specimen_to_laboratory :bool
    consultant_surgeon :str
    co_surgeon :str
    surgeon :str
    anesthetist :str
    nurse :str 
    sponge_nurse :str
    doctor_name:str







"""class ProfileSchemaOut(Schema):
    pk : UUID4
    name : str 
    age : str 
    weight :  str 
    gender : str
    number : str
    Ward : str
    Bed : str"""