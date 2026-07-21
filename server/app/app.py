# from fastapi import FastAPI

# from server.app.api import (
#     auth,
#     websocket,
#     meeting,
#     conversation,
# )


# app = FastAPI()


# app.include_router(
#     auth.router,
#     prefix="/api"
# )

# app.include_router(
#     websocket.router,
#     prefix="/api"
# )

# app.include_router(
#     meeting.router,
#     prefix="/api"
# )

# app.include_router(
#     conversation.router,
#     prefix="/api"
# )


# @app.on_event("startup")
# async def debug_routes():

#     print("\n========== FINAL APP ROUTES ==========")

#     for route in app.routes:
#         print(
#             type(route),
#             getattr(route, "path", None)
#         )

#     print("======================================")

from fastapi import FastAPI
from server.app.api import auth, websocket, meeting, conversation

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(websocket.router, prefix="/api")
app.include_router(meeting.router, prefix="/api")
app.include_router(conversation.router, prefix="/api")