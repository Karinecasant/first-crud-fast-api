from fastapi import FastAPI

from .rests import routers

app = FastAPI()

for router in routers:
    app.include_router(router)
