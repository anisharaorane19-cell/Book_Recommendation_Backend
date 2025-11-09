from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base

# ---------------- USER ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    ratings = relationship("Rating", back_populates="user")
    favorites = relationship("Favorite", back_populates="user")


# ---------------- BOOK ----------------
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    genre = Column(String(50))
    avg_rating = Column(Float, default=0)

    ratings = relationship("Rating", back_populates="book")


# ---------------- RATING ----------------
class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    rating = Column(Float, nullable=False)

    user = relationship("User", back_populates="ratings")
    book = relationship("Book", back_populates="ratings")


# ---------------- FAVORITE ----------------
class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    user = relationship("User", back_populates="favorites")
    book = relationship("Book")
