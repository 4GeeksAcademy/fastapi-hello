from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..utils import APIException
from ..models import Base, User
from pydantic import BaseModel, Field, EmailStr
from passlib.context import CryptContext

router = APIRouter()

# Serializers are used to validate the incoming request body
# Here you determine which fields are required and their types
class CreateSerializer(BaseModel):
    password: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    is_active: bool

# Serializers are also used to format the outgoing response body
class UserSmallSerializer(BaseModel):
    email: str
    is_active: bool

    class Config:
        from_attributes = True

# EXAMPLE ON HOW TO LIST ALL THE DATABASE USERS
    
@router.get('/user')
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    response_body = {
        "msg": "Hello, this is your GET /user response, check the data property on this payload ",
        "data": [UserSmallSerializer.model_validate(user) for user in users]
    }

    return response_body


# EXAMPLE ON HOW TO RETRIVE A SINGLE USER BY ID

@router.get("/user/{user_id}")
def read_single_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise APIException("User not found", status_code=404)
    return user.serialize()


# EXAMPLE ON HOW TO CREATE A NEW USER


@router.post("/user")
def create_user(payload: CreateSerializer, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == payload.email).first()
    if user:
        raise APIException("User already found with this email", status_code=404)

    # We start by hashing the password
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(payload.password)

    # Then we create the user and commit
    db_user = User(email=payload.email, is_active=True, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()

    return payload