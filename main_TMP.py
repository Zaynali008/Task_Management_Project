from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

tasks = [ {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Practice CRUD endpoints",
    "completed": False},
{
    "id": 2,
    "title": "Learn Git and GitHub",
    "description": "Practice till professional team work",
    "completed": False},
    {
    "id": 3,
    "title": "Learn Leetcode Foundation",
    "description": "Practice leet code style problems to solve actual leet code problems ",
    "completed": True},
]

class TaskRequest(BaseModel):
    
    title: str
    description: str
    completed: bool

class TaskPatch(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=50)
    description: str |None = Field(default=None, min_length=3, max_length=300)
    completed: bool | None = None

@app.patch("/tasks/{id}")
def create_patch(id: int, task: TaskPatch):
    for item in tasks:
        if item["id"]== id:
            if task.title is not None:
                item["title"] = task.title
            if task.description is not None:
                item["description"] = task.description
            if task.completed is not None:
                item["completed"] = task.completed
            return item

    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )

@app.post("/tasks")
def create_new_task(task: TaskRequest):
    new_id = tasks[-1]["id"] +1
    new_task = task.model_dump()
    new_task["id"] = new_id
    tasks.append(new_task)
    
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
    status_code=404,
    detail="Task not found"
)

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return task
        
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
@app.put("/tasks/{id}")
def update_task(id: int, task: TaskRequest):
    for task in tasks:
        if task["id"] == id:
            task["title"] = task.title
            task["description"] = task.description
            task["completed"] = task.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="Not Found"
    )

@app.get("/alltask")
def all_task():
    return tasks

print("Starting with Git/GitHub on 10 oct")
print("Starting with Git/GitHub on 10 oct")