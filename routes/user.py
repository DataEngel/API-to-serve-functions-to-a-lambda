from fastapi import APIRouter
from config.db import conn
from models.user import predictions

user = APIRouter()  

@user.get("/ver_registros")
def get_predictions():
    return conn.execute(predictions.select()).fetchall()


