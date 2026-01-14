from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import hash_password, verify_password,create_access_token

def register_user(db: Session, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def login_user(user: User):
    access_token = create_access_token(data={"sub": user.email})
    return access_token