from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory DB as list
student_dict = []

class Student(BaseModel):
    id: int
    name: str
    cls: str
    age: int
    gender: str
    country: str
    address: str
    subjects: list[str]

@app.get("/")
def welcome():
    return {"message": "Hey there! Welcome to MK-Classes"}
         
@app.post("/add-student/")
def add_student(item: Student):
    for val in student_dict:
        if val.id == item.id:
            return { "message": "Student already found.", "data": val }

    student_dict.append(item)
    return { "message": "Displaying new student info.", "data": item }

@app.post("/update-student/{id}")
def update_student(id: int, item: Student):
    for i in range(len(student_dict)):
        if student_dict[i].id == id:
            student_dict[i]=item
            return { "message": "Displaying updated student info.", "data": student_dict[i] }

    return { "message": "Student not found." }

@app.get("/student/{id}")
def get_student(id: int):
    for val in student_dict:
        if val.id == id:
            return { "message": "Displaying info of student.", "data": val }
        
    return { "message": "Student not found." }

@app.get("/get-all-students/")
def get_all_students():
    return { "message": "Displaying info of all students.", "data": student_dict }

@app.post("/delete-student/{id}")
def delete_student(id: int):
    for i in range(len(student_dict)):
        if student_dict[i].id == id:
            # remove by index
            student_dict.pop(i)
            return { "message": "Deleted info of student."}

    return { "message": "Student not found." }
