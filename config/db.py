from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root01@localhost:3306/risk_predictions_two_db")

meta = MetaData()

conn = engine.connect() 
