from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import User
from schemas import UserCreate, UserLogin
from passlib.context import CryptContext
import hashlib

router = APIRouter(prefix="/auth", tags=["Authentication"])

# bcrypt context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ SIGNUP route
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Step 1: Convert to bytes and hash with SHA256 first (handles ANY password length)
    sha_hashed = hashlib.sha256(user.password.encode("utf-8")).hexdigest()

    # Step 2: bcrypt hash the SHA result (always 64 bytes, safe!)
    hashed_pw = pwd_context.hash(sha_hashed)

    new_user = User(email=user.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


# ✅ LOGIN route
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email")

   
    sha_hashed = hashlib.sha256(user.password.encode("utf-8")).hexdigest()

    # Step 2: Verify bcrypt against stored hash
    if not pwd_context.verify(sha_hashed, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {"message": "Login successful"}
