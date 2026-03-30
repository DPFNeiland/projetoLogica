from fastapi import FastAPI
from services.problem_service import load_problem



app = FastAPI()

@app.get("/problem/{problem_id}")
def get_problem(problem_id: int):
    data = load_problem(problem_id)
    return data