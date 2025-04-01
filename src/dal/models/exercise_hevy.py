from pydantic import BaseModel, Field

from .set_hevy import SetHevy


class ExerciseHevy(BaseModel):
    """
    Exercise Model from Hevy API
    """

    index: int = Field(
        None,
        description="Index indicating the order of the exercise in the workout",
        examples=[0],
    )
    title: str = Field(
        None,
        description="Title of the exercise",
        examples=["Bench Press"],
    )
    notes: str = Field(
        "",
        description="Notes on the exercise",
        examples=["Paid closer attention to form today. Felt great!"],
    )
    supersets_id: int | None = Field(
        None,
        description="The id of the superset that the exercise belongs to. A value of null indicates the exercise is not part of a superset.",
        examples=[0],
    )

    # TODO -> implement SET
    sets: list[SetHevy] = Field(
        [],
    )
