from fastapi import APIRouter
from modules.auth.schemas.login_schema import (
    LoginWithCredentialsRequestSchema,
    LoginWithCredentialsResponseSchema,
)

router = APIRouter()


@router.post(
    "/login/credentials",
    response_model=LoginWithCredentialsResponseSchema,
    summary="Login with credentials",
)
def login(request: LoginWithCredentialsRequestSchema):
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}
