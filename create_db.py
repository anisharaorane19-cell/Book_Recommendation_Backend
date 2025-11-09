from db_config import Base, engine
from models import User, Book, Rating,Favorite
from sqlalchemy import inspect

print("Checking existing tables...")

# Create a database inspector
inspector = inspect(engine)
existing_tables = inspector.get_table_names()

# Show existing tables
print("Existing tables:", existing_tables)

# Create only missing 'users' table
if "users" not in existing_tables:
    print("Creating missing 'users' table...")
    User.__table__.create(bind=engine)
    print("✅ 'users' table created successfully!")
else:
    print("✅ 'users' table already exists, skipping creation.")

print("All done!")
