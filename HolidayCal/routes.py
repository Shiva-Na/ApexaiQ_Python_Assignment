from fastapi import APIRouter
from models import HolidayRequest
import requests

router = APIRouter()


class HolidayService:

    BASE = "https://date.nager.at/api/v3/PublicHolidays"

    def fetch(self, year: int, country: str):
        country = country.strip().upper()

        url = f"{self.BASE}/{year}/{country}"
        print("DEBUG URL:", url)

        try:
            resp = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0"
            })
        except Exception as e:
            return {"holidays": [], "error": str(e)}

        print("STATUS:", resp.status_code)
        print("RESPONSE:", resp.text[:200])  # first 200 chars

        if resp.status_code == 204:
            return {"holidays": [], "error": "No data available (204 from API)"}

        if resp.status_code != 200:
            return {"holidays": [], "error": "API request failed"}

        try:
            data = resp.json()
        except Exception:
            return {"holidays": [], "error": "Invalid JSON response"}

        holidays = [
            {
                "name": h.get("name"),
                "date": h.get("date")
            }
            for h in data
        ]

        return {"holidays": holidays}


@router.post("/holidays")
def get_holidays(data: HolidayRequest):
    print("Country:", data.country)
    print("Year:", data.year)

    svc = HolidayService()
    return svc.fetch(data.year, data.country)