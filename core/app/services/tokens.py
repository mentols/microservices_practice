import logging
from datetime import timedelta, datetime

import jwt
from fastapi import HTTPException
from starlette import status

from config import Config

logger = logging.getLogger(__name__)


class TokenServices:
    @staticmethod
    def create_response(request_id, code, message):
        """
        Function to create a response to be sent back via the API
        :param request_id:Id fo the request
        :param code:Error Code to be used
        :param message:Message to be sent via the APi
        :return:Dict with the above given params
        """
        try:
            req = str(request_id)
            data = {"data": message, "code": int(code), "request_id": req}
            return data
        except Exception as creation_error:
            logger.error(f'create_response:{creation_error}')

    @staticmethod
    async def decode_access_jwt_token(authorization):
        if not authorization:
            response = TokenServices.create_response(
                "3",
                401,
                {"message": "Authorization not found, Please send valid token in headers"}
            )
            logger.info(f"Response {response}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            token = authorization.split()[1]
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=Config.ALGORITHM)
            return data.get('id')
        except jwt.ExpiredSignatureError:
            response = TokenServices.create_response("1", 401, {"message": "Authentication token has expired"})
            logger.info(f"Response {response}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication token has expired",
            )
        except (jwt.DecodeError, jwt.InvalidTokenError):
            response = TokenServices.create_response(
                "2",
                401,
                {"message": "Authorization has failed, Please send valid token."}
            )
            logger.info(f"Response {response}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication token has expired",
            )

    @staticmethod
    async def decode_refresh_jwt_token(refresh_token):
        try:
            payload = jwt.decode(refresh_token, Config.SECRET_KEY, algorithms=Config.ALGORITHM)
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has expired",
            )
        return payload.get('id')
