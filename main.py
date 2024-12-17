from fastapi import FastAPI
from routers import user_router
from database import engine
import models.user

# Create database tables
models.user.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include Routers
app.include_router(user_router.router, prefix="/users", tags=["Users"])
