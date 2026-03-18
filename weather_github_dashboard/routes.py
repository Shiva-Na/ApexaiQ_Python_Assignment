from fastapi import APIRouter
from models import CityRequest, RepoRequest
import requests

router = APIRouter()

API_KEY = "512c04058a15613c23dcbe16645f9274"


class WeatherService:
    """Retrieve weather data from OpenWeatherMap."""

    BASE = "https://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city: str):
        url = f"{self.BASE}?q={city}&appid={API_KEY}&units=metric"
        resp = requests.get(url).json()
        return {"city": city, "temperature": resp["main"]["temp"], "description": resp["weather"][0]["description"]}


class GitHubService:
    """Retrieve GitHub repository statistics."""

    def stats(self, owner: str, repo: str):
        url = f"https://api.github.com/repos/{owner}/{repo}"
        resp = requests.get(url).json()
        return {"repository": repo, "stars": resp.get("stargazers_count"), "forks": resp.get("forks_count"), "open_issues": resp.get("open_issues_count")}


@router.post("/weather")
def get_weather(data: CityRequest):
    """Endpoint delegating to WeatherService."""
    return WeatherService().fetch(data.city)


@router.post("/github")
def github_stats(data: RepoRequest):
    """Endpoint delegating to GitHubService."""
    return GitHubService().stats(data.owner, data.repo)