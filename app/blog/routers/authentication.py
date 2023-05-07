from fastapi import APIRouter, Depends, Form
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..repository import authentication
from ..schemas import UserRegistrationSchema
from pyfa_converter import PyFaDepends


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authentication.login(request, db)


@router.post('/register')
def register(request: UserRegistrationSchema,
             db: Session = Depends(get_db)):
    return authentication.register(request, db)

