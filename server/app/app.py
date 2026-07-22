from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.app.api.route import router
from server.app.services.Fathom import fathom_handler

cors_allowed_origins = [ "http://localhost:3000", "http://localhost:5678"]

app = FastAPI()


app.include_router(router=router, prefix="/api")

# fathom_handler.create_webhook()
# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins= cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)