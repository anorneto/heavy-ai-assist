from typing import Optional

from pydantic import BaseModel, Field

from .exercise_hevy import ExerciseHevy


class WorkoutHevy(BaseModel):
    id: str = Field(
        None,
        description="The unique identifier for the workout. Seens to be a UUID4?",
        example="b459cba5-cd6d-463c-abd6-54f8eafcadcb",
    )
    title: str = Field(None, description="The workout title.", example="Friday Leg Day 🔥")
    description: Optional[str] = Field(
        "",
        description="The workout description.",
        example="Medium intensity leg day focusing on quads.",
    )
    start_time: str = Field(
        None,
        description="ISO 8601 timestamp of when the workout was recorded to have started",
        example="2024-08-14T12:00:00Z",
    )
    end_time: str = Field(
        None,
        description="ISO 8601 timestamp of when the workout was recorded to have ended.",
        example="2024-08-14T12:30:00Z",
    )
    updated_at: str = Field(None, description="ISO 8601 timestamp of when the workout was last updated.")
    created_at: str = Field(None, description="ISO 8601 timestamp of when the workout was created.")
    exercises: list[ExerciseHevy] = Field([], description="A list of exercises in the workout.")
