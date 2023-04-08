from bson import ObjectId
from pydantic import BaseModel, Field

from app.serializers.pages import PyObjectId


class Page(BaseModel):
    _id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    page_id: int
    task_amount: int
    resolved: int
    unresolved: int
    resolution_percentage: float

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
