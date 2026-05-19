from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.database.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

def get_auth_service(db=Depends(get_db)):
    return AuthService(db)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, service: AuthService = Depends(get_auth_service)):
    return await service.register_user(user_in)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(get_auth_service)):
    return await service.authenticate_user(form_data.username, form_data.password)

@router.get("/test")
async def test_auth():
    return {"message": "Auth funcionando"}