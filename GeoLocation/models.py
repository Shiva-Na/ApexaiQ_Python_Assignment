from pydantic import BaseModel


class IPRequest(BaseModel):
    """Request model for IP geolocation lookup."""
    ip: str