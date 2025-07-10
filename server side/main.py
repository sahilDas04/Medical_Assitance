from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Medical Assitance API', description='An API for medical chatbot')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.middleware("http")(catch_exception_middleware)

app.include_router(upload_router)

app.include_router(ask_router)