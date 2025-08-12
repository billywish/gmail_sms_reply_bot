import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Email
from config import os

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_email(
    recipient, 
    subject, 
    received_content, 
    generated_reply, 
    status='pending', 
    message_id=None
    ):
    session = SessionLocal()
    email_record = Email(
        recipient=recipient,
        subject=subject,
        received_content=received_content,
        generated_reply=generated_reply,
        status=status,
        message_id=message_id
    )
    session.add(email_record)
    session.commit()
    email_id = email_record.id  # access before closing session
    session.close()
    
    return email_id

def get_email_by_id(email_id):
    session = SessionLocal()
    email_record = session.query(Email).filter(Email.id == email_id).first()
    session.close()
    if email_record:
        return {
            'recipient': email_record.recipient,
            'subject': email_record.subject,
            'received_content': email_record.received_content,
            'generated_reply': email_record.generated_reply,
            'status': email_record.status,
            'message_id': email_record.message_id
        }
    return None


def update_email_status(email_id, new_status):
    session = SessionLocal()
    email_record = session.query(Email).filter(Email.id == email_id).first()
    if email_record:
        email_record.status = new_status
        session.commit()
    session.close()
