
# Description
This is a simple app created using Python FastAPI to demonstrate basic CRUD operations using local in-memory cache. This API has endpoints to create a new student, update an existing student, show details of a student by its id, show details of all students and delete a specific student by id.

# Steps
## Install python
```
apt install python3.12-venv
```

## Create virtual env
```
python3 -m venv venv
```

## Activate venv
```
source venv/bin/activate
```

## Install packages
```
pip install fastapi
pip install uvicorn
```

## Start the app locally
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Call the Api
```
curl -X 'POST' \
  'https://4c505d4cb013-10-244-5-88-8000.papa.r.killercoda.com/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "akash",
  "cls": "10A",
  "age": 25,
  "gender": "male",
  "country": "India",
  "address": "kolkata",
  "subjects": [
    "physics",
    "chemistry",
    "maths"
  ]
}'
```
