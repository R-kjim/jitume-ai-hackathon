from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    auth,
    websocket,
    meeting,
    conversation,
)


app = FastAPI()


# ============================
# CORS CONFIGURATION
# ============================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],
)



# ============================
# API ROUTES
# ============================

app.include_router(
    auth.router,
    prefix="/api"
)

app.include_router(
    websocket.router,
    prefix="/api"
)

app.include_router(
    meeting.router,
    prefix="/api"
)

app.include_router(
    conversation.router,
    prefix="/api"
)



# ============================
# DEBUG ROUTES
# ============================

@app.on_event("startup")
async def debug_routes():

    print("\n========== FINAL APP ROUTES ==========")

    for route in app.routes:
        print(
            getattr(route, "methods", None),
            getattr(route, "path", None)
        )

    print("======================================")
    