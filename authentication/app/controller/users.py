from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.users import UserRepository
from app.schemas.users import UserIn as UserSchemaIn
from app.services.tokens import TokenServices


class UserController:
    @staticmethod
    async def sign_in(user: UserSchemaIn, session: AsyncSession):
        tasks = await UserRepository.create_user(user.dict(), session)
        return tasks

    @staticmethod
    async def refresh_token(refresh_token, session: AsyncSession):
        user_id = await TokenServices.decode_refresh_jwt_token(refresh_token)
        user = await UserRepository.get_user_by_id(user_id, session)
        return await TokenServices(user).generate_response()

    @staticmethod
    async def sign_up(user: UserSchemaIn, session: AsyncSession):
        user = await UserRepository.get_user(user, session)
        return await TokenServices(user).generate_response()

    @staticmethod
    async def update_user(user, session: AsyncSession):
        await UserRepository.update_user(user, session)
