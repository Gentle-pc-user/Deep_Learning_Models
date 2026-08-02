from pydantic import BaseModel, Field
from typing import Annotated


class PredictionResponse(BaseModel):
    predicted_price: Annotated[float, Field(
        ..., 
        description="Predicted house price in Lakh INR",
        example=85.5
    )]
    currency: Annotated[str, Field(..., example="Lakh INR")]
    confidence: Annotated[str, Field(..., example="High")]
    model_version: Annotated[str, Field(..., example="1.0.0")]