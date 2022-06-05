from pydantic import BaseModel 

class User(BaseModel):
    id: int
    age: int
    years_on_the_job: int
    nb_previous_loans: int
    avg_amount_loans_previous: int
    flag_own_car: int