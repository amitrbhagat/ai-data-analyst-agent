from typing import Literal
from pydantic import BaseModel, Field



class RoutingResult(BaseModel):

    route: Literal["SQl", "RAG", "HYBRID"]
    reasoning: str
    confidence: float = Field(
        ge=0.0,
        le=1.0
    )
    