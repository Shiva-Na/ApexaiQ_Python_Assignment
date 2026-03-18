from fastapi import APIRouter
from models import MovieRequest
import requests

router = APIRouter()

API_KEY = "936c0f37"


class MovieService:
    """Interact with OMDb for movie search."""

    BASE = "http://www.omdbapi.com/"

    def search(self, query: str, page: int = 1, year: int | None = None):
        url = f"{self.BASE}?apikey={API_KEY}&s={query}&page={page}"
        if year:
            url += f"&y={year}"
        resp = requests.get(url).json()
        if resp.get("Response") == "False":
            return {"error": resp.get("Error")}
        movies = [
            {"title": m["Title"], "year": m["Year"], "type": m["Type"], "poster": m["Poster"]}
            for m in resp.get("Search", [])
        ]
        return {"total_results": resp.get("totalResults"), "page": page, "movies": movies}


@router.post("/search")
def search_movies(data: MovieRequest):
    """Endpoint delegating to MovieService."""
    svc = MovieService()
    return svc.search(data.query, data.page, data.year)