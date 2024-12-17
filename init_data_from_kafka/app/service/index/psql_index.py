from sqlalchemy import create_engine, Index, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateIndex, DropIndex

# Using Declarative Models
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(50))
    age = Column(Integer)

    # Create index directly in model
    __table_args__ = (
        Index('idx_email', 'email', unique=True),
        Index('idx_username_age', 'username', 'age'),  # Compound index
        Index('idx_age', 'age', postgresql_where=age > 18),  # Partial index (Postgres)
    )


# Creating indexes after model definition
Index('idx_username', User.username)

users = Table('users', MetaData,
              Column('id', Integer, primary_key=True),
              Column('email', String(255)),
              Column('username', String(50)),
              Column('age', Integer)
              )

# Create indexes on existing table
email_idx = Index('idx_email', users.c.email, unique=True)
compound_idx = Index('idx_username_age', users.c.username, users.c.age)
