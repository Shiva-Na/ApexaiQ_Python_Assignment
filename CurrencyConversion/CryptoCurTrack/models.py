from pydantic import BaseModel


class CryptoRequest(BaseModel):
    """Request model for crypto price lookup."""
    coin: str
    currency: str = "usd"