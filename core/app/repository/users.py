from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette import status

from app.models.users import User
from app.schemas.users import User as UserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRepository:
    @staticmethod
    async def create_user(user: dict, session: AsyncSession) -> UserSchema:
        print(user.get('password'))
        password = pwd_context.hash(user.get('password'))
        print(password)
        user = User(username=user.get('username'), password=password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def get_user_by_id(user_id, session: AsyncSession) -> UserSchema:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    @staticmethod
    async def get_user(user, session: AsyncSession) -> UserSchema:
        try:
            result = await session.execute(select(User).where(User.username == user.username))
            result_user = result.scalars().first()
            expected_user = UserSchema(
                id=result_user.id,
                username=result_user.username,
                password=result_user.password
            )

            if pwd_context.verify(user.password, expected_user.password):
                return expected_user
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect credentials",
                )
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect credentials",
            )

    @staticmethod
    async def update_user(user, session: AsyncSession) -> None:
        query = (
            update(User).where(User.id == User).values(**user).execution_options(synchronize_session="fetch")
        )

        await session.execute(query)
        await session.commit()

        return user
