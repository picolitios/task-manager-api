from fastapi import HTTPException, status
from app.schemas.user_schema import UserCreate
from app.models.user import UserModel
from app.core.security import get_password_hash, verify_password, create_access_token

class AuthService:
    def __init__(self, db):
        self.collection = db.users

    async def register_user(self, user_in: UserCreate):
        # Check if email exists
        existing_user = await self.collection.find_one({"email": user_in.email})
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash password and save
        hashed_password = get_password_hash(user_in.password)
        new_user = UserModel(email=user_in.email, hashed_password=hashed_password)
        
        result = await self.collection.insert_one(new_user.to_dict())
        
        return {
            "id": str(result.inserted_id),
            "email": new_user.email,
            "created_at": new_user.created_at
        }

    async def authenticate_user(self, email: str, password: str):
        user = await self.collection.find_one({"email": email})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not verify_password(password, user["hashed_password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        user_id = str(user["_id"])
        access_token = create_access_token(subject=email, user_id=user_id)
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
