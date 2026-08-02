from pydantic import BaseModel, Field, field_validator
from typing import Annotated


class HouseInput(BaseModel):
    area_type: Annotated[str, Field(..., description="Area Type")]
    availability: Annotated[str, Field(..., description="Availability")]
    location: Annotated[str, Field(..., description="Location")]
    size: Annotated[str, Field(..., description="Size (e.g. 2 BHK)")]
    society: Annotated[str, Field("", description="Society (optional)")]
    total_sqft: Annotated[float, Field(..., gt=0)]
    bath: Annotated[float, Field(..., gt=0)]
    balcony: Annotated[float, Field(..., ge=0)]

    @field_validator('location', 'size', 'society', 'area_type', 'availability')
    @classmethod
    def normalize_strings(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v

    class Config:
        extra = "ignore"        # ← Important: ignore extra fields
        str_strip_whitespace = True