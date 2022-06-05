from fastapi import APIRouter
from config.db import conn
from models.user import predictions
from schemas.user import User
from typing import List

user = APIRouter()  

@user.get(
    "/users", 
    tags=["users"], 
    response_model=List[User],
    description="Get a list of all users",
    )
def get_predictions():
    return conn.execute(predictions.select()).fetchall()

@user.post(
    "/",
    tags=["users"], 
    response_model=User, 
    description="Create a new user"
    )
def create_user(user: User): 
    new_user = {
    "id": user.id, 
    "age": user.age, 
    "years_on_the_job": user.years_on_the_job, 
    "nb_previous_loans": user.nb_previous_loans,
    "avg_amount_loans_previous": user.avg_amount_loans_previous,
    "flag_own_car": user.flag_own_car
    }
    result = conn.execute(predictions.insert().values(new_user))
    return conn.execute(predictions.select().where(predictions.c.id == result.lastrowid)).first()


@user.get(
    "/users_by_id/{id}",
    tags=["users"],
    response_model=User,
    description="Get a single user by Id",
)

def get_user(id: str):
    return conn.execute(predictions.select().where(predictions.c.id == id)).first()
