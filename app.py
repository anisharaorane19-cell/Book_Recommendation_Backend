from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db_config import SessionLocal, engine
from models import Base, Book
from pydantic import BaseModel
from auth import router as auth_router  # Import once
from favorites import router as favorites_router


# Create the app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency for DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Book Recommendation System backend is running successfully!"}

# ✅ Include auth routes with a prefix
app.include_router(auth_router)
app.include_router(favorites_router)



# Book routes
@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return jsonable_encoder(books)

@app.get("/recommend/{topic}")
def recommend_books(topic: str, db: Session = Depends(get_db)):
    books = db.query(Book).filter(
        (Book.genre.ilike(f"%{topic}%")) |
        (Book.title.ilike(f"%{topic}%")) |
        (Book.author.ilike(f"%{topic}%"))
    ).all()

    if not books:
        return {"message": "No books found for this topic."}
    return jsonable_encoder(books)

# Run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000,reload=True)