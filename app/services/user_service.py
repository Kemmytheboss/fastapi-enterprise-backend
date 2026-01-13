from  sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import hash_password

def create_user(db: Session, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user