from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class LoginWithCredentialsRequestSchema(BaseModel):
    email: EmailStr = Field(
        description="User's email address", examples=["neymar@example.com"]
    )
    password: str = Field(description="User's password", examples=["password123"])

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if not re.match(pattern, value):
            raise ValueError(
                "Password must be at least 8 characters long and contain at least one letter and one number."
            )

        return value


class LoginWithCredentialsResponseSchema(BaseModel):
    access_token: str = Field(description="JWT access token")
    token_type: str = Field(description="Type of the token, usually 'bearer'")
