from pydantic import BaseModel


class QuoteResponse(BaseModel):
    """Response model for quote endpoint."""
    quote: str
    author: str