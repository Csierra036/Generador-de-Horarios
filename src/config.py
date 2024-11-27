from pydantic_settings import BaseSettings

#Variables declared in .env are defined here to be used. The variable in .env must be the same as the one that 
# will be placed in the class 
class Settings(BaseSettings):
    URL_DATABASE: str


settings = Settings()