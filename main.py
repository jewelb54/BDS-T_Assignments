from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json


app = FastAPI()


#Create an patient class
class Patient_profile(BaseModel):
    resourcetype="patient"
    identifier:int
    active: bool
    name: str

@app.get("/")
async def first_api():
    return {"message": "Hello Kazi"}

@app.post("/patient/{patient_id}")
async def patient(patient:Patient_profile,patient_id:int ):
    with open ("patient_profile", 'r+') as infile:
        patient_db =json.load(infile)
    patient_db[patient_id] = patient.dict()


    
