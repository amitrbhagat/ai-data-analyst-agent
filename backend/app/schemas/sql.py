# Here define the format we expect TinyLlama to return.

from pydantic import BaseModel, Field

class SQLGenerationResult(BaseModel):

    sql: str
    reasoning_summary : str
    confidence: float = Field(ge=0.0, le=1.0)


