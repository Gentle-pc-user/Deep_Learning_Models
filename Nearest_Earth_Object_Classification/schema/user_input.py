from pydantic import BaseModel, Field
from typing import List

class UserInput(BaseModel):
    est_diameter_min: float = Field(..., gt=-1, lt=38, description="Minimum Estimated Diameter in Kilometres")
    est_diameter_max: float = Field(..., gt=-1, lt=85, description="Maximum Estimated Diameter in Kilometres")
    relative_velocity: float = Field(..., gt=200, lt=246990, description="Velocity Relative to Earth")
    miss_distance: float = Field(..., gt=1000, description="Distance in Kilometres missed")
    sentry_object: bool = Field(default=False, description="Included in sentry - an automated collision monitoring system")
    absolute_magnitude: float = Field(..., gt=8.50, lt=34, description="Describes intrinsic luminosity")

    def to_tensor_list(self) -> List[float]:
        # Convert boolean sentry_object to 1.0 or 0.0 for the neural network
        sentry_val = 1.0 if self.sentry_object else 0.0
        return [
            self.est_diameter_min,
            self.est_diameter_max,
            self.relative_velocity,
            self.miss_distance,
            sentry_val,
            self.absolute_magnitude
        ]