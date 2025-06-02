from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data=json.load(file)
        return data
    
@app.get("/")
def Hello():
    return {'message' : 'hello everyone'}

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
# def view_patient(patient_id :str ):
def view_patient(patient_id: str = Path(..., descrription = "Id of the patienton in the DB", example='P001')):

    data= load_data() 

    if patient_id in data:
        return data[patient_id]
    else:
        return {'error' : 'patient_id not found'}
    