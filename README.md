# Data Management System API

A Data-based RESTful API for managing patient records with BMI calculation functionality.

## Features

- Create, read, update, and delete patient records
- Automatic BMI calculation and health verdict
- Sorting patients by height, weight, or BMI
- Data persistence in JSON format
- Input validation and error handling

## API Endpoints

### Base URLs
- `GET /` - Welcome message
- `GET /about` - API description

### Patient Operations
- `GET /view` - View all patients
- `GET /patient/{patient_id}` - View specific patient
- `POST /create` - Create new patient
- `PUT /edit/{patient_id}` - Update existing patient
- `DELETE /delete/{patient_id}` - Delete patient

### Sorting
- `GET /sort` - Sort patients by height, weight, or BMI (asc/desc)

## Data Model

### Patient Object
```json
{
  "id": "string (required, unique)",
  "name": "string (required)",
  "city": "string (required)",
  "age": "integer (required, 0 < age < 120)",
  "gender": "string (required, 'male'|'female'|'others')",
  "height": "float (required, >0 in meters)",
  "weight": "float (required, >0 in kg)",
  "bmi": "float (computed)",
  "verdict": "string (computed: 'Underweight'|'Normal'|'Obese')"
}

```
### Installation
1.  Clone the repository
2.  Install dependencies:

```
pip install fastapi uvicorn
```
3. Run the server:
```
uvicorn main:app --reload
```

- Create Patient
```
curl -X POST "http://localhost:8000/create" \
-H "Content-Type: application/json" \
-d '{
  "id": "P001",
  "name": "John Doe",
  "city": "New York",
  "age": 30,
  "gender": "male",
  "height": 1.75,
  "weight": 70
}'
```
- Update Patient
```
curl -X PUT "http://localhost:8000/edit/P001" \
-H "Content-Type: application/json" \
-d '{
  "weight": 72,
  "city": "Boston"
}'
```

- Sort Patients by BMI (descending)
```
curl "http://localhost:8000/sort?sort_by=bmi&order=desc"
```
### Error Handling
The API returns appropriate HTTP status codes:

- 200: Success

- 201: Created

- 400: Bad request (invalid input)

- 404: Not found

- 422: Validation error

### Dependencies
- Python 3.7+

- FastAPI

- Pydantic

- Uvicorn (for running the server)