from fastapi import APIRouter
from models import NewsRequest
import requests

router = APIRouter()

API_KEY = "74db731a3eb0441ebb0f55c09187882c"


class NewsService:
    """Fetch headlines from NewsAPI."""

    BASE = "https://newsapi.org/v2/top-headlines"

    def headlines(self, country: str = "us", category: str | None = None):
        url = f"{self.BASE}?country={country}&apiKey={API_KEY}"
        if category:
            url += f"&category={category}"
        resp = requests.get(url).json()
        if resp.get("status") != "ok":
            return {"error": "Unable to fetch news"}
        articles = [
            {"title": a["title"], "source": a["source"]["name"], "url": a["url"], "image": a["urlToImage"]}
            for a in resp.get("articles", [])[:10]
        ]
        return {"total_results": resp.get("totalResults"), "articles": articles}


@router.post("/news")
def get_news(data: NewsRequest):
    """Endpoint delegating to NewsService."""
    svc = NewsService()
    return svc.headlines(data.country, data.category)