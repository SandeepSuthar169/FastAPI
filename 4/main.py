from fastapi import FastAPI, HTTPException, Query
import json
from pydantic import BaseModel,Field, computed_field
from typing import Annotated, Literal
from pathlib import Path

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", examples=['POO1'])]
    name: Annotated[str, Field(..., description='name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=90, description='Age of the patient')]
    gender: Annotated[Literal['male', 'felale', 'other'], Field(..., description='gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='height of the patient in mtrs')]
    weight: Annotated[float, Field(..., ft= 0, description='weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi  = round(self.weight)/ (self.height**2)
        return bmi
    

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"
        



def load_data():
    with open('patients.json', 'r') as file:
      data = json.load(file)
      
      return data

@app.get("/")
def hello():
    return {'message':' get page'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
# def view_patient(patient_id :str ):
def view_patient(patient_id: str = Path(..., description = "Id of the patienton in the DB", example='P001')):

    data= load_data() 

    if patient_id in data:
        return data[patient_id]
    else:
        #return {'error' : 'patient_id not found'}
        return HTTPException(status_code=404,detail="patient not found")
    


@app.get("/sort")
def sort_patinets(sort_by: str = Query(..., description="sort by the basis of height, weight on bmi"), order: str = Query('asc',description='sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid filed select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get('sort_by', 0), reverse= sort_order)

#                                                                     reverse = False -> asc order
#                                                                     reverse = True  -> desc order


    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):
    pass








       # 24:31