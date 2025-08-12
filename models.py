from enum import Enum
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class EmailStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    DISCARDED = "discarded"
    REJECTED = "rejected"  # Feedback needed / needs redraft

class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipient = Column(String(255), nullable=False)
    subject = Column(String(255))
    received_content = Column(Text)       # Original email text received from sender
    generated_reply = Column(Text)        # AI-generated draft/reply
    message_id = Column(String(255), nullable=True, unique=False)
    status = Column(String(50), nullable=False, default=EmailStatus.PENDING.value)
    created_at = Column(DateTime, server_default=func.now())