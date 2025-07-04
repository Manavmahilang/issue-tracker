from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, issues

app = FastAPI()

# Enable CORS for SvelteKit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(issues.router, prefix="/issues", tags=["issues"])
