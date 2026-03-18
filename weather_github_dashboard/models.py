from pydantic import BaseModel


class CityRequest(BaseModel):
    """Request model for city weather lookups."""
    city: str


class RepoRequest(BaseModel):
    """Request model for GitHub repo stats."""
    owner: str
    repo: str