

from fastapi import FastAPI, Request
from routes import router
import time
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()


@app.middleware("http")
async def log_request(request: Request, call_next):
    print("Middleware started")

    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start

    print(f"Request {request.url}  took {process_time:.3f} seconds to process.")

    return response



app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to the Product API!"}
