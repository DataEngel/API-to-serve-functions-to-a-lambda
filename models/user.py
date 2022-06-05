from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine

predictions = Table("predictions", meta,

    Column("id", Integer, primary_key=True),
    Column("age", Integer),
    Column("years_on_the_job", Integer),
    Column("nb_previous_loans", Integer),
    Column("avg_amount_loans_previous", Integer),
    Column("flag_own_car", Integer),
)

meta.create_all(engine)