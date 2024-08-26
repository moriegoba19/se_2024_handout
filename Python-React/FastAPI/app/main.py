from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Allow React frontend to communicate with FastAPI backend
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")

def read_root():
    return {"message": "Welcome to the FastAPI Backend"}


@app.get("/api")
def read_api():
    return {"message": "This is the API endpoint"}

