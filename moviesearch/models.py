from pydantic import BaseModel


class MovieRequest(BaseModel):
    """Request model for movie search."""
    query: str
    page: int = 1
    year: int | None = None