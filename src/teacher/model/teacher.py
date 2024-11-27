from pydantic import BaseModel
from typing import Optional

class Teacher(BaseModel):
    id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

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