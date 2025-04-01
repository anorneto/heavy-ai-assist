# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-04-01T01:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Workout(BaseModel):
    title: Optional[str] = Field(
        None, description="The title of the workout.", example="Friday Leg Day 🔥"
    )
    description: Optional[str] = Field(
        None,
        description="A description for the workout workout.",
        example="Medium intensity leg day focusing on quads.",
    )
    start_time: Optional[str] = Field(
        None,
        description="The time the workout started.",
        example="2024-08-14T12:00:00Z",
    )
    end_time: Optional[str] = Field(
        None, description="The time the workout ended.", example="2024-08-14T12:30:00Z"
    )
    is_private: Optional[bool] = Field(
        None,
        description="A boolean indicating if the workout is private.",
        example=False,
    )
    exercises: Optional[List[PostWorkoutsRequestExercise]] = None


class PostWorkoutsRequestBody(BaseModel):
    workout: Optional[Workout] = None


class PostRoutinesRequestSet(BaseModel):
    type: Optional[Type] = Field(
        None, description="The type of the set.", example="normal"
    )
    weight_kg: Optional[float] = Field(
        None, description="The weight in kilograms.", example=100
    )
    reps: Optional[int] = Field(
        None, description="The number of repetitions.", example=10
    )
    distance_meters: Optional[int] = Field(None, description="The distance in meters.")
    duration_seconds: Optional[int] = Field(
        None, description="The duration in seconds."
    )
    custom_metric: Optional[float] = Field(
        None,
        description="A custom metric for the set. Currently used for steps and floors.",
    )


class PostRoutinesRequestExercise(BaseModel):
    exercise_template_id: Optional[str] = Field(
        None, description="The ID of the exercise template.", example="D04AC939"
    )
    superset_id: Optional[int] = Field(None, description="The ID of the superset.")
    rest_seconds: Optional[int] = Field(
        None, description="The rest time in seconds.", example=90
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes for the exercise.",
        example="Stay slow and controlled.",
    )
    sets: Optional[List[PostRoutinesRequestSet]] = None


class Routine(BaseModel):
    title: Optional[str] = Field(
        None, description="The title of the routine.", example="April Leg Day 🔥"
    )
    folder_id: Optional[float] = Field(
        None,
        description='The folder id the routine should be added to. Pass null to insert the routine into default "My Routines" folder',
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes for the routine.",
        example="Focus on form over weight. Remember to stretch.",
    )
    exercises: Optional[List[PostRoutinesRequestExercise]] = None


class PostRoutinesRequestBody(BaseModel):
    routine: Optional[Routine] = None


class PutRoutinesRequestSet(BaseModel):
    type: Optional[Type] = Field(
        None, description="The type of the set.", example="normal"
    )
    weight_kg: Optional[float] = Field(
        None, description="The weight in kilograms.", example=100
    )
    reps: Optional[int] = Field(
        None, description="The number of repetitions.", example=10
    )
    distance_meters: Optional[int] = Field(None, description="The distance in meters.")
    duration_seconds: Optional[int] = Field(
        None, description="The duration in seconds."
    )
    custom_metric: Optional[float] = Field(
        None,
        description="A custom metric for the set. Currently used for steps and floors.",
    )


class PutRoutinesRequestExercise(BaseModel):
    exercise_template_id: Optional[str] = Field(
        None, description="The ID of the exercise template.", example="D04AC939"
    )
    superset_id: Optional[int] = Field(None, description="The ID of the superset.")
    rest_seconds: Optional[int] = Field(
        None, description="The rest time in seconds.", example=90
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes for the exercise.",
        example="Stay slow and controlled.",
    )
    sets: Optional[List[PutRoutinesRequestSet]] = None


class Routine1(BaseModel):
    title: Optional[str] = Field(
        None, description="The title of the routine.", example="April Leg Day 🔥"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes for the routine.",
        example="Focus on form over weight. Remember to stretch.",
    )
    exercises: Optional[List[PutRoutinesRequestExercise]] = None


class PutRoutinesRequestBody(BaseModel):
    routine: Optional[Routine1] = None


class RoutineFolder(BaseModel):
    title: Optional[str] = Field(
        None,
        description="The title of the routine folder.",
        example="Push Pull 🏋️\u200d♂️",
    )


class PostRoutineFolderRequestBody(BaseModel):
    routine_folder: Optional[RoutineFolder] = None


class ExerciseTemplate(BaseModel):
    id: Optional[str] = Field(
        None,
        description="The exercise template ID.",
        example="b459cba5-cd6d-463c-abd6-54f8eafcadcb",
    )
    title: Optional[str] = Field(
        None, description="The exercise title.", example="Bench Press (Barbell)"
    )
    type: Optional[str] = Field(
        None, description="The exercise type.", example="weight_reps"
    )
    primary_muscle_group: Optional[str] = Field(
        None,
        description="The primary muscle group of the exercise.",
        example="weight_reps",
    )
    secondary_muscle_groups: Optional[List[str]] = Field(
        None, description="The secondary muscle groups of the exercise."
    )
    is_custom: Optional[bool] = Field(
        None,
        description="A boolean indicating whether the exercise is a custom exercise.",
        example=False,
    )


class RoutineFolder1(BaseModel):
    id: Optional[float] = Field(None, description="The routine folder ID.", example=42)
    index: Optional[float] = Field(
        None,
        description="The routine folder index. Describes the order of the folder in the list.",
        example=1,
    )
    title: Optional[str] = Field(
        None, description="The routine folder title.", example="Push Pull 🏋️\u200d♂️"
    )
    updated_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the folder was last updated.",
        example="2021-09-14T12:00:00Z",
    )
    created_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the folder was created.",
        example="2021-09-14T12:00:00Z",
    )


class Set(BaseModel):
    index: Optional[float] = Field(
        None,
        description="Index indicating the order of the set in the routine.",
        example=0,
    )
    type: Optional[str] = Field(
        None,
        description="The type of set. This can be one of 'normal', 'warmup', 'dropset', 'failure'",
        example="normal",
    )
    weight_kg: Optional[float] = Field(
        None, description="Weight lifted in kilograms.", example=100
    )
    reps: Optional[float] = Field(
        None, description="Number of reps logged for the set", example=10
    )
    distance_meters: Optional[float] = Field(
        None, description="Number of meters logged for the set"
    )
    duration_seconds: Optional[float] = Field(
        None, description="Number of seconds logged for the set"
    )
    rpe: Optional[float] = Field(
        None,
        description="RPE (Relative perceived exertion) value logged for the set",
        example=9.5,
    )
    custom_metric: Optional[float] = Field(
        None,
        description="Custom metric logged for the set (Currently only used to log floors or steps for stair machine exercises)",
        example=50,
    )


class Exercise(BaseModel):
    index: Optional[float] = Field(
        None,
        description="Index indicating the order of the exercise in the routine.",
        example=0,
    )
    title: Optional[str] = Field(
        None, description="Title of the exercise", example="Bench Press (Barbell)"
    )
    notes: Optional[str] = Field(
        None,
        description="Routine notes on the exercise",
        example="Focus on form. Go down to 90 degrees.",
    )
    exercise_template_id: Optional[str] = Field(
        None,
        description="The id of the exercise template. This can be used to fetch the exercise template.",
        example="05293BCA",
    )
    supersets_id: Optional[float] = Field(
        None,
        description="The id of the superset that the exercise belongs to. A value of null indicates the exercise is not part of a superset.",
        example=0,
    )
    sets: Optional[List[Set]] = None


class Routine2(BaseModel):
    id: Optional[str] = Field(
        None,
        description="The routine ID.",
        example="b459cba5-cd6d-463c-abd6-54f8eafcadcb",
    )
    title: Optional[str] = Field(
        None, description="The routine title.", example="Upper Body 💪"
    )
    folder_id: Optional[float] = Field(
        None, description="The routine folder ID.", example=42
    )
    updated_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the routine was last updated.",
        example="2021-09-14T12:00:00Z",
    )
    created_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the routine was created.",
        example="2021-09-14T12:00:00Z",
    )
    exercises: Optional[List[Exercise]] = None


class Set1(BaseModel):
    index: Optional[float] = Field(
        None,
        description="Index indicating the order of the set in the workout.",
        example=0,
    )
    type: Optional[str] = Field(
        None,
        description="The type of set. This can be one of 'normal', 'warmup', 'dropset', 'failure'",
        example="normal",
    )
    weight_kg: Optional[float] = Field(
        None, description="Weight lifted in kilograms.", example=100
    )
    reps: Optional[float] = Field(
        None, description="Number of reps logged for the set", example=10
    )
    distance_meters: Optional[float] = Field(
        None, description="Number of meters logged for the set"
    )
    duration_seconds: Optional[float] = Field(
        None, description="Number of seconds logged for the set"
    )
    rpe: Optional[float] = Field(
        None,
        description="RPE (Relative perceived exertion) value logged for the set",
        example=9.5,
    )
    custom_metric: Optional[float] = Field(
        None,
        description="Custom metric logged for the set (Currently only used to log floors or steps for stair machine exercises)",
        example=50,
    )


class Exercise1(BaseModel):
    index: Optional[float] = Field(
        None,
        description="Index indicating the order of the exercise in the workout.",
        example=0,
    )
    title: Optional[str] = Field(
        None, description="Title of the exercise", example="Bench Press (Barbell)"
    )
    notes: Optional[str] = Field(
        None,
        description="Notes on the exercise",
        example="Paid closer attention to form today. Felt great!",
    )
    exercise_template_id: Optional[str] = Field(
        None,
        description="The id of the exercise template. This can be used to fetch the exercise template.",
        example="05293BCA",
    )
    supersets_id: Optional[float] = Field(
        None,
        description="The id of the superset that the exercise belongs to. A value of null indicates the exercise is not part of a superset.",
        example=0,
    )
    sets: Optional[List[Set1]] = None


class Workout1(BaseModel):
    id: Optional[str] = Field(
        None,
        description="The workout ID.",
        example="b459cba5-cd6d-463c-abd6-54f8eafcadcb",
    )
    title: Optional[str] = Field(
        None, description="The workout title.", example="Morning Workout 💪"
    )
    description: Optional[str] = Field(
        None,
        description="The workout description.",
        example="Pushed myself to the limit today!",
    )
    start_time: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the workout was recorded to have started.",
        example="2021-09-14T12:00:00Z",
    )
    end_time: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the workout was recorded to have ended.",
        example="2021-09-14T12:00:00Z",
    )
    updated_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the workout was last updated.",
        example="2021-09-14T12:00:00Z",
    )
    created_at: Optional[str] = Field(
        None,
        description="ISO 8601 timestamp of when the workout was created.",
        example="2021-09-14T12:00:00Z",
    )
    exercises: Optional[List[Exercise1]] = None


class UpdatedWorkout(BaseModel):
    type: str = Field(
        ..., description="Indicates the type of the event (updated)", example="updated"
    )
    workout: Workout1


class DeletedWorkout(BaseModel):
    type: str = Field(
        ..., description="Indicates the type of the event (deleted)", example="deleted"
    )
    id: str = Field(
        ...,
        description="The unique identifier of the deleted workout",
        example="efe6801c-4aee-4959-bcdd-fca3f272821b",
    )
    deleted_at: Optional[str] = Field(
        None,
        description="A date string indicating when the workout was deleted",
        example="2021-09-13T12:00:00Z",
    )


class PaginatedWorkoutEvents(BaseModel):
    page: int = Field(..., description="The current page number", example=1)
    page_count: int = Field(
        ..., description="The total number of pages available", example=5
    )
    events: List[Union[UpdatedWorkout, DeletedWorkout]] = Field(
        ..., description="An array of workout events (either updated or deleted)"
    )
