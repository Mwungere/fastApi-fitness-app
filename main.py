from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal
from hashing import Hasher

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency: Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create User
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    hashed_password = Hasher.get_password_hash(user.password);
    # Create new user
    new_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.post("/users/login", response_model=schemas.LoginResponse)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not Hasher.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": "Logged in successfully",
        "user": db_user
    }

# Read Users
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Read User by ID
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user details
    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password
    db.commit()
    db.refresh(user)
    return user

# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}

