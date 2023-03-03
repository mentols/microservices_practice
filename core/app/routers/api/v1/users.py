from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.controller.users import UserController
from app.database.db import get_session
from app.schemas.tokens import RefreshToken as RefreshTokenSchema
from app.schemas.tokens import Token as TokenSchema
from app.schemas.users import User as UserSchema
from app.schemas.users import UserIn as UserSchemaIn

api_router = APIRouter()


@api_router.post('/sign_in', response_model=UserSchema)
async def sign_in(user: UserSchemaIn, session: AsyncSession = Depends(get_session)):
    user = await UserController.sign_in(user, session)
    return user


@api_router.post('/refresh', response_model=TokenSchema)
async def refresh_token(token: RefreshTokenSchema, session: AsyncSession = Depends(get_session)):
    tokens = await UserController.refresh_token(token, session)
    return tokens


@api_router.post('/sign_up', response_model=TokenSchema)
async def sign_up(user: UserSchemaIn, session: AsyncSession = Depends(get_session)):
    tokens = await UserController.sign_up(user, session)
    return tokens


@api_router.put('/update')
async def update_user(user: UserSchemaIn, session: AsyncSession = Depends(get_session)):
    user = await UserController.update_user(user, session)
    return user
