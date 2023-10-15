import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.logger import Logger
from src.routers import users

app = FastAPI()
logger = Logger(__file__)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request, call_next):
    logger.debug(f"Request: {request.method} {request.url} {request.client.host} {request.client.port}")
    response = await call_next(request)
    logger.debug(f"Response: {response.status_code} {response.headers}")
    return response

### Routers ###
app.include_router(
    router = users.router,
    prefix = "/users",
    tags = ["users"],
    responses = {404: {"description": "Not found"}},
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)