from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# Every table in the database will have its corresponding model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    # Make sure to hash the password before saving it
    hashed_password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username