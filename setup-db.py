import argparse
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Warning: If the reset flag is true, any data in the todos table will be deleted

# Create an ArgumentParser instance
parser = argparse.ArgumentParser()
# Add an argument called 'reset' which will be a boolean flag
parser.add_argument('--reset', action='store_true')
# Parse the arguments passed to the script
args = parser.parse_args()

# Create an engine to connect to the SQLite database file
engine = create_engine('sqlite:///todos.db')

# Create a session to use the engine
Session = sessionmaker(bind=engine)
session = Session()

# Define the base for the declarative ORM
Base = declarative_base()

class Todos(Base):
  __tablename__ = 'todos'

  id = Column(Integer, primary_key=True)
  task = Column(String)
  completed = Column(Boolean, default=False)

  def __repr__(self):
    return f"<Todo(id={self.id}, task={self.task}, completed={self.completed})>"

# Check the connection status
try:
  engine.connect()
  print('Connection to the SQLite database has been established successfully.')
except Exception as err:
  print(f'Unable to connect to the SQLite database: {err}')

# Delete the todos table if the reset flag is set
if args.reset:
  Todos.__table__.drop(engine)

# Create the todos table
Base.metadata.create_all(engine)

# Create a todo
todo = Todos(task='Test Todo 123', completed=False)
session.add(todo)
session.commit()

# Query todos
todos = session.query(Todos).all()
print(f'{len(todos)} todos found')