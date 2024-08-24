from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from todo.dto.user import Token, UserCreate, UserResponse
from todo.services.user import *
from todo.utils import create_access_token, get_password_hash

router = APIRouter()


@router.post("/token", response_model=Token, tags=['users'])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=UserResponse, tags=['users'])
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, name=user.name, password=hashed_password, role_id=user.role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/me", response_model=UserResponse, tags=['users'])
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
