from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import Favorite, User, Book

router = APIRouter(prefix="/favorites", tags=["Favorites"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add/{email}/{book_id}")
def add_to_favorites(email: str, book_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    book = db.query(Book).filter(Book.id == book_id).first()

    if not user or not book:
        raise HTTPException(status_code=404, detail="User or Book not found")

    existing_fav = db.query(Favorite).filter(
        Favorite.user_id == user.id, Favorite.book_id == book.id
    ).first()

    if existing_fav:
        raise HTTPException(status_code=400, detail="Already added to favorites")

    new_fav = Favorite(user_id=user.id, book_id=book.id)
    db.add(new_fav)
    db.commit()
    return {"message": "✅ Book added to favorites!"}


@router.get("/list/{email}")
def list_favorites(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    favorites = (
        db.query(Book)
        .join(Favorite, Favorite.book_id == Book.id)
        .filter(Favorite.user_id == user.id)
        .all()
    )

    return favorites


@router.delete("/remove/{email}/{book_id}")
def remove_favorite(email: str, book_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    fav = db.query(Favorite).filter(
        Favorite.user_id == user.id, Favorite.book_id == book_id
    ).first()

    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(fav)
    db.commit()
    return {"message": "❌ Book removed from favorites"}
