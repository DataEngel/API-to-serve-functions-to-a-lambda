from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta, engine

predictions = Table("predictions_table", meta,
    Column("id", Integer, primary_key=True),
    Column("years_on_the_job", Integer),
    Column("nb_previous_loans", Integer),
    Column("avg_amount_loans_previous", Integer),
    Column("flag_own_car", Integer),
)

meta.create_all(engine)