from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel

class Career(Base):
    __tablename__ = "careers"
    id = Column(Integer, primary_key = True, index = True)
    fullname = Column(String, index = True)
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "fullname": "Ingenieria en Informatica"
                }
            ]
        }
    }


class CreateCareerRequest(BaseModel):
    fullname: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "fullname": "Ingenieria en Informatica",
                }
            ]
        }
    }