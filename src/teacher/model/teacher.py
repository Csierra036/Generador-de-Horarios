from src.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey, Column
from pydantic import BaseModel

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key = True, index = True)
    first_name = Column(String, index = True)
    last_name = Column(String, index = True)
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Juan",
                    "last_name": "Pedro"
                },
            ]
        }
    }


class CreateTeacherRequest(BaseModel):
    first_name: str
    last_name: str
    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Juan",
                    "last_name": "Pedro"
                },
            ]
        }
    }