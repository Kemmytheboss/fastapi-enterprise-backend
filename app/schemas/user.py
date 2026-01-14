from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72,
        description="Password must be between 8 and 72 characters",
    )

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72,
        description="Password must be between 8 and 72 characters",
    )

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        form_attributes = True