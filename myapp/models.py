from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    """A user of the app."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)

    def __init__(self, username, email):
        """Create instance."""
        self.username = username
        self.email = email

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User(username: {self.username!r}, id: {self.id})>"
