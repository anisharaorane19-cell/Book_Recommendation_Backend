

from db_config import SessionLocal, engine, Base   # ✅ this line imports Base correctly
from models import Book

# Create all tables if not already created
Base.metadata.create_all(bind=engine)

session = SessionLocal()



books = [
    # 💖 Love / Romance
    Book(title="Pride and Prejudice", author="Jane Austen", genre="Love"),
    Book(title="The Notebook", author="Nicholas Sparks", genre="Romance"),
    Book(title="Me Before You", author="Jojo Moyes", genre="Love"),
    Book(title="It Ends With Us", author="Colleen Hoover", genre="Romance"),

    # 💸 Finance / Business
    Book(title="Rich Dad Poor Dad", author="Robert Kiyosaki", genre="Finance"),
    Book(title="The Intelligent Investor", author="Benjamin Graham", genre="Finance"),
    Book(title="The Psychology of Money", author="Morgan Housel", genre="Finance"),
    Book(title="Think and Grow Rich", author="Napoleon Hill", genre="Finance"),

    # 💡 Self-Improvement / Motivation
    Book(title="Atomic Habits", author="James Clear", genre="Self-Improvement"),
    Book(title="The Power of Habit", author="Charles Duhigg", genre="Self-Improvement"),
    Book(title="Deep Work", author="Cal Newport", genre="Productivity"),
    Book(title="The Subtle Art of Not Giving a F*ck", author="Mark Manson", genre="Motivation"),
    Book(title="Can't Hurt Me", author="David Goggins", genre="Motivation"),

    # 🧠 Psychology
    Book(title="Thinking, Fast and Slow", author="Daniel Kahneman", genre="Psychology"),
    Book(title="Man’s Search for Meaning", author="Viktor Frankl", genre="Psychology"),

    # 🧬 Science / Technology
    Book(title="A Brief History of Time", author="Stephen Hawking", genre="Science"),
    Book(title="The Selfish Gene", author="Richard Dawkins", genre="Science"),
    Book(title="Superintelligence", author="Nick Bostrom", genre="Technology"),
    Book(title="AI 2041", author="Kai-Fu Lee", genre="Artificial Intelligence"),
    Book(title="Clean Code", author="Robert C. Martin", genre="Programming"),

    # 🚀 Startups / Entrepreneurship
    Book(title="Zero to One", author="Peter Thiel", genre="Startup"),
    Book(title="The Lean Startup", author="Eric Ries", genre="Startup"),
    Book(title="The Hard Thing About Hard Things", author="Ben Horowitz", genre="Business"),

    # 🧩 Philosophy / Spiritual
    Book(title="Meditations", author="Marcus Aurelius", genre="Philosophy"),
    Book(title="The Alchemist", author="Paulo Coelho", genre="Spirituality"),
    Book(title="The Bhagavad Gita", author="Vyasa", genre="Philosophy"),

    # 🏛 History / Society
    Book(title="Sapiens", author="Yuval Noah Harari", genre="History"),
    Book(title="The Diary of a Young Girl", author="Anne Frank", genre="History"),
    Book(title="Guns, Germs, and Steel", author="Jared Diamond", genre="History"),

    # 🖥 Education / Learning
    Book(title="Educated", author="Tara Westover", genre="Biography"),
    Book(title="Outliers", author="Malcolm Gladwell", genre="Education"),

    # 🎨 Art / Creativity
    Book(title="Steal Like an Artist", author="Austin Kleon", genre="Art"),
    Book(title="Big Magic", author="Elizabeth Gilbert", genre="Creativity"),

    # 🩺 Health / Lifestyle
    Book(title="Why We Sleep", author="Matthew Walker", genre="Health"),
    Book(title="The 4-Hour Body", author="Tim Ferriss", genre="Health"),
    Book(title="Ikigai", author="Héctor García", genre="Lifestyle"),

    # ⚽ Sports / Teamwork
    Book(title="Relentless", author="Tim Grover", genre="Sports"),
    Book(title="Shoe Dog", author="Phil Knight", genre="Sports"),

    # 🌍 Environment / Future
    Book(title="The Sixth Extinction", author="Elizabeth Kolbert", genre="Environment"),
    Book(title="This Changes Everything", author="Naomi Klein", genre="Environment"),

    # 👩‍💼 Leadership / Productivity
    Book(title="Start With Why", author="Simon Sinek", genre="Leadership"),
    Book(title="Leaders Eat Last", author="Simon Sinek", genre="Leadership")
]

session.add_all(books)
session.commit()
session.close()

print("✅ 40 diverse topic-based books inserted successfully!")