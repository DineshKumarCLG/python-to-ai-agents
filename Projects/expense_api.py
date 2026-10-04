from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Expense tracker with API")

class Expense(BaseModel):
    category: str
    amount: float = Field(gt=0, description="Amount must be positive")
    description: str = ""

# expenses = []

@app.get("/")
def root():
    return {"message":"Expense Tracker API is running!"}

@app.post("/expenses", status_code=201)
# def add_expense(expense: Expense):
#     expenses.append(expense.model_dump())
#     return {"message":"Expense added successfully", "data": expense}
def add_expense(expense: Expense, db: Session=Depends(get_db)):
    db_expense=models.Expense(
        category=expense.category,
        amount=expense.amount,
        description=expense.description
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses", status_code=200)
# def get_all_expenses():
#     if not expenses:
#         raise HTTPException(status_code=404, detail="No expenses found")
#     return {"count":len(expenses), "expenses":expenses}
def get_all_expenses(db: Session=Depends(get_db)):
    all_expenses=db.query(models.Expense).all()
    if not all_expenses:
         raise HTTPException(status_code=404, detail="No expenses found")
    return{"count":len(all_expenses), "expenses": all_expenses}

@app.get("/expenses/highest", status_code=200)
# def get_highest_expenses():
#     if not expenses:
#         raise HTTPException(status_code=404, detail="No expenses found")
#     highest = max(expenses, key=lambda x:x["amount"])
#     return {"highest_expense": highest}

def get_highest_expenses(db: Session=Depends(get_db)):
    highest_expense=db.query(models.Expense).order_by(models.Expense.amount.desc()).first()
    if not highest_expense:
        raise HTTPException(status_code=404, detail="No expenses found")
    return {"highest_expense": highest_expense}

@app.delete("/expenses/{expense_id}",status_code=200)
def delete_expense(expense_id: int, db: Session=Depends(get_db)):
    expense=db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")
    db.delete(expense)
    db.commit()
    return {"message": f"Expense {expense_id} deleted successfully"}

@app.put("/expenses/{expense_id}", status_code=200)
def update_expense(expense_id: int, updated_data: Expense, db:Session=Depends(get_db)):
    expense=db.query(models.Expense).filter(models.Expense.id==expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail=f"Expense with id {expense_id} not found")

    expense.category=updated_data.category
    expense.amount=updated_data.amount
    expense.description=updated_data.description

    db.commit()
    db.refresh(expense)
    return expense