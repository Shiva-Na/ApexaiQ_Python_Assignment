from pydantic import BaseModel


class NewsRequest(BaseModel):
    """Request model for top headlines."""
    country: str = "us"
    category: str | None = None