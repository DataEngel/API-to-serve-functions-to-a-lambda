from fastapi import FastAPI
from routes.user import user
from config.openapi import tags_metadata

app = FastAPI(
    title="API to serve the features",
    description="A REST api to insert the feature engineering data and to extract and send that same data to the model",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)