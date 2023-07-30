from datetime import datetime

from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.api_core.v1.utils import decode_jwe


class ApiBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request:Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication method"
                )

            if not self.ckeck(credentials.credentials):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token or expired token")

            return credentials.credentials
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid auth"
            )

    def ckeck(self, jwtoken: str) -> bool:
        try:
            payload = decode_jwe(jwtoken)
        except Exception as e:
            return False
        else:
            valid_true = payload.get("valid_true")
            return datetime.strptime(valid_true, "%Y-%m-%d %H:%M:%S.%f") > datetime.now()
