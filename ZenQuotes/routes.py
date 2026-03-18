from fastapi import APIRouter
import requests
from datetime import date

router = APIRouter()


class QuoteService:
    """Fetch and cache daily quote from ZenQuotes."""

    API = "https://zenquotes.io/api/today"
    _cache = {"date": None, "quote": None, "author": None}

    def today(self):
        today = str(date.today())
        if self._cache["date"] == today:
            return {"quote": self._cache["quote"], "author": self._cache["author"], "source": "cache"}
        resp = requests.get(self.API)
        if resp.status_code != 200:
            return {"error": "Failed to fetch quote"}
        data = resp.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        self._cache.update({"date": today, "quote": quote, "author": author})
        return {"quote": quote, "author": author, "source": "api"}


@router.get("/quote")
def get_quote():
    """Endpoint delegating to QuoteService."""
    return QuoteService().today()