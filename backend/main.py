import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from api.chat import router as chat_router

load_dotenv()

app = FastAPI(title="University Chatbot API")

# Optional: Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the /chat route
app.include_router(chat_router)


