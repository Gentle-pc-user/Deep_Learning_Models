from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_category: bool = Field(
        ...,
        description="Boolean feature that shows whether asteroid is harmful (True) or not (False)"
    )
    probability: float = Field(
        ...,
        description="Model's confidence score for the object being hazardous (range: 0 to 1)"
    )