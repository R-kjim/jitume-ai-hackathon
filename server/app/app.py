from fastapi import FastAPI
from server.app.api.route import router

app = FastAPI()


app.include_router(router=router, prefix="/api")





