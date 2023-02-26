from pydantic import BaseModel, BaseSettings, Field


class TestUser(BaseModel):
    email: str
    password: str


class Settings(BaseSettings):
    base_url: str = Field(..., env='BASE_URL')
    user_email: str = Field(..., env='TEST_USER_EMAIL')
    user_password: str = Field(..., env='TEST_USER_PASSWORD')