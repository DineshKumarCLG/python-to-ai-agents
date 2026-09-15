from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Expense tracker with API")

class Expense(BaseModel):
    category: str
    amount: float = Field(gt=0, description="Amount must be positive")
    description: str = ""

expenses = []

@app.get("/")
def root():
    return {"message":"Expense Tracker API is running!"}

@app.post("/expenses", status_code=201)
def add_expense(expense: Expense):
    expenses.append(expense.model_dump())
    return {"message":"Expense added successfully", "data": expense}

@app.get("/expenses", status_code=200)
def get_all_expenses():
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")
    return {"count":len(expenses), "expenses":expenses}
    
@app.get("/expenses/highest", status_code=200)
def get_highest_expenses():
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")
    highest = max(expenses, key=lambda x:x["amount"])
    return {"highest_expense": highest}