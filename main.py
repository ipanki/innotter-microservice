from fastapi import FastAPI
from microservice.views import routes_user

app = FastAPI()
app.include_router(routes_user, prefix="/service")