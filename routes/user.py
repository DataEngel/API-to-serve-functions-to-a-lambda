from fastapi import APIRouter
from config.db import conn
from models.user import predictions
from schemas.user import User
from typing import List
from lambda_in.inboke_lambda_docker import inboke_lambda_1
import json

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

def get_user_one(id: str):
    return conn.execute(predictions.select().where(predictions.c.id == id)).first() 

@user.get(
    "/send_by_id/{id}",
    tags=["users"],
    response_model=User,
    description="send a single user by Id",
)
def get_user(id: str):
    query = conn.execute(predictions.select().where(predictions.c.id == id)).first()
    values_query = query 

    id_ = values_query.id
    id_main = str(id_) 

    inputParamss = {
        id_main : {
            "1": values_query.age,
            "2": values_query.years_on_the_job,
            "3": values_query.nb_previous_loans,
            "4": values_query.avg_amount_loans_previous,
            "5": values_query.flag_own_car
        }
    }
    
    lambda_returns = inboke_lambda_1(inputParamss)

    print("Lambda returns: ", lambda_returns)

    return query

