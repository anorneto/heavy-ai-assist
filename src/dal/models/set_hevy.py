from pydantic import BaseModel, Field
from .rpe_hevy import RpeHevy
from .set_type_hevy import SetTypeHevy


class SetHevy(BaseModel):
    """
    Set Model from Hevy API
    """

    index: int = Field(
        None, description="Index indicating the order of the set in the exercise", examples=[0]
    )
    type: SetTypeHevy = Field(None, description="Type of the set", examples=["normal"])
    weight_kg: float | None = Field(None, description="Weight lifted in kilograms", examples=[100.0])
    reps: int | None = Field(None, description="Number of reps logged for the set", examples=[10])
    distance_meters: float | None = Field(
        None, description="Number of meters logged for the set", examples=[None]
    )
    durations_seconds: int | None = Field(
        None, description="Number of seconds logged for the set", examples=[None]
    )
    rpe: RpeHevy | None = Field(
        None, description="RPE (Relative perceived exertion) value logged for the set", examples=[9.5]
    )
    custom_metric: float | None = Field(
        None,
        description="Custom metric logged for the set (Currently only used to log floors or steps for stair machine exercises)",
        examples=[50],
    )
