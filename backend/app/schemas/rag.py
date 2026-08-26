from pydantic import BaseModel, Field


class RAGAnswerResult(BaseModel):
    answer: str = Field(
        description="Answer based only on the retrieved context."
    )

    sources: list[str] = Field(
        default_factory=list,
        description="Source filenames used to answer the question."
    )

    grounded: bool = Field(
        description="Whether the answer is supported by the retrieved context."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence that the answer is supported by the context."
    )

    