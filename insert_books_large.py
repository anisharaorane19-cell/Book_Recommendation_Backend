from db_config import SessionLocal
from models import Book

db = SessionLocal()

# 100+ Books across 10+ genres
books = [
    # --- LOVE / ROMANCE ---
    ("Pride and Prejudice", "Jane Austen", "romance", 4.8),
    ("The Notebook", "Nicholas Sparks", "love", 4.3),
    ("Me Before You", "Jojo Moyes", "romance", 4.4),
    ("The Time Traveler’s Wife", "Audrey Niffenegger", "romance", 4.2),
    ("The Fault in Our Stars", "John Green", "romance", 4.6),

    # --- MOTIVATION / SELF-HELP ---
    ("Atomic Habits", "James Clear", "motivation", 4.8),
    ("The Power of Now", "Eckhart Tolle", "self-help", 4.7),
    ("The Subtle Art of Not Giving a F*ck", "Mark Manson", "self-help", 4.3),
    ("Think Like a Monk", "Jay Shetty", "motivation", 4.4),
    ("You Are a Badass", "Jen Sincero", "self-help", 4.5),

    # --- FINANCE / BUSINESS ---
    ("The Intelligent Investor", "Benjamin Graham", "finance", 4.7),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "business", 4.6),
    ("The Psychology of Money", "Morgan Housel", "finance", 4.6),
    ("Think and Grow Rich", "Napoleon Hill", "business", 4.5),
    ("Zero to One", "Peter Thiel", "startup", 4.4),
    ("The Lean Startup", "Eric Ries", "entrepreneurship", 4.5),

    # --- SCIENCE / TECHNOLOGY / AI ---
    ("A Brief History of Time", "Stephen Hawking", "science", 4.7),
    ("Astrophysics for People in a Hurry", "Neil deGrasse Tyson", "astronomy", 4.6),
    ("AI Superpowers", "Kai-Fu Lee", "artificial intelligence", 4.5),
    ("Deep Learning", "Ian Goodfellow", "technology", 4.7),
    ("Machine Learning Yearning", "Andrew Ng", "AI", 4.6),
    ("Life 3.0", "Max Tegmark", "AI", 4.5),

    # --- HEALTH / FITNESS ---
    ("Why We Sleep", "Matthew Walker", "health", 4.8),
    ("Can’t Hurt Me", "David Goggins", "fitness", 4.8),
    ("Born to Run", "Christopher McDougall", "fitness", 4.5),
    ("The 4-Hour Body", "Tim Ferriss", "health", 4.4),
    ("How Not to Die", "Michael Greger", "nutrition", 4.6),

    # --- HISTORY / CULTURE ---
    ("Sapiens", "Yuval Noah Harari", "history", 4.8),
    ("Homo Deus", "Yuval Noah Harari", "future", 4.6),
    ("Guns, Germs, and Steel", "Jared Diamond", "civilization", 4.5),
    ("The Silk Roads", "Peter Frankopan", "history", 4.4),
    ("The Diary of a Young Girl", "Anne Frank", "biography", 4.7),

    # --- FANTASY / FICTION ---
    ("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", "fantasy", 4.9),
    ("The Hobbit", "J.R.R. Tolkien", "fantasy", 4.8),
    ("Percy Jackson & the Olympians", "Rick Riordan", "adventure", 4.7),
    ("The Hunger Games", "Suzanne Collins", "fiction", 4.7),
    ("Dune", "Frank Herbert", "sci-fi", 4.6),

    # --- MYSTERY / THRILLER ---
    ("The Girl with the Dragon Tattoo", "Stieg Larsson", "mystery", 4.5),
    ("Gone Girl", "Gillian Flynn", "thriller", 4.6),
    ("The Da Vinci Code", "Dan Brown", "thriller", 4.4),
    ("Sherlock Holmes: The Complete Novels", "Arthur Conan Doyle", "mystery", 4.8),
    ("The Silent Patient", "Alex Michaelides", "psychological", 4.4),

    # --- EDUCATION / LEARNING ---
    ("Educated", "Tara Westover", "memoir", 4.7),
    ("The 7 Habits of Highly Effective People", "Stephen Covey", "education", 4.7),
    ("Outliers", "Malcolm Gladwell", "learning", 4.6),
    ("Drive", "Daniel H. Pink", "psychology", 4.5),
    ("Mindset", "Carol S. Dweck", "growth", 4.6),

    # --- PHILOSOPHY / SPIRITUALITY ---
    ("Meditations", "Marcus Aurelius", "philosophy", 4.7),
    ("The Art of Happiness", "Dalai Lama", "spirituality", 4.6),
    ("The Prophet", "Kahlil Gibran", "poetry", 4.5),
    ("Man’s Search for Meaning", "Viktor Frankl", "psychology", 4.8),
    ("The Bhagavad Gita", "Vyasa", "spirituality", 4.9),
]

count = 0
for title, author, genre, rating in books:
    existing = db.query(Book).filter(Book.title == title).first()
    if not existing:
        db.add(Book(title=title, author=author, genre=genre, avg_rating=rating))
        count += 1

db.commit()
db.close()

print(f"✅ Inserted {count} new books successfully (duplicates skipped)!")
