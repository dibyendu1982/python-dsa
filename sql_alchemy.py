# 
# pip install sqlalchemy psycopg2

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Replace with your credentials
DATABASE_URI = "postgresql+psycopg2://user:password@localhost:5432/mydb"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()



from sqlalchemy import asc, desc

# Example model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Fetch all users sorted by name ascending
users = session.query(User).order_by(asc(User.name)).all()

# Sort by multiple columns (name asc, id desc)
users = session.query(User).order_by(asc(User.name), desc(User.id)).all()

from sqlalchemy import select, MetaData, Table

metadata = MetaData()
users_table = Table('users', metadata, autoload_with=engine)

# Basic sorted query
stmt = select(users_table).order_by(users_table.c.name)
results = session.execute(stmt).fetchall()

# With raw SQL
stmt = text("SELECT * FROM users ORDER BY name DESC")
results = session.execute(stmt).fetchall()
