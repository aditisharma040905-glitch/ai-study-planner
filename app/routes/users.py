from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import UserCreate, UserLogin
from app.core.auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)
from datetime import timedelta

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Temporary in-memory database
fake_users_db = []

# =====================
# SIGNUP
# =====================
@router.post("/signup")
def signup(user: UserCreate):
    for u in fake_users_db:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)

    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password,
        "role": "user"
    }

    fake_users_db.append(new_user)
    return {"message": "User created successfully"}

# =====================
# LOGIN
# =====================
@router.post("/login")
def login(user: UserLogin):
    for u in fake_users_db:
        if u["email"] == user.email:
            if not verify_password(user.password, u["password"]):
                raise HTTPException(status_code=401, detail="Incorrect password")

            token = create_access_token(
                data={"sub": u["email"]},
                expires_delta=timedelta(minutes=30)
            )

            return {
                "access_token": token,
                "token_type": "bearer"
            }

    raise HTTPException(status_code=404, detail="User not found")

# =====================
# PROTECTED ROUTE
# =====================
@router.get("/me")
def get_me(current_user: str = Depends(verify_token)):
    return {"email": current_user}
