from fastapi import FastAPI, Path, HTTPException, Query
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