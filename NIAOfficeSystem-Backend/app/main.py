from fastapi import FastAPI
from app.routes import login, cases

app = FastAPI()

app.include_router(login.router)
app.include_router(cases.router)
