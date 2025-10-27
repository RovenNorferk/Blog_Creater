from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to access posts by this user
    posts = relationship("Post", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"
    
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # Increased length for practicality
    content = Column(String(5000), nullable=False)  # Use larger limit instead of Text for control
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to access the user who created this post
    user = relationship("User", back_populates="posts")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title})>"