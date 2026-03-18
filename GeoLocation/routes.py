from fastapi import APIRouter
from models import IPRequest
import requests

router = APIRouter()


class GeoService:
    """Lookup IP geolocation using ip-api."""

    BASE = "http://ip-api.com/json"

    def lookup(self, ip: str):
        resp = requests.get(f"{self.BASE}/{ip}")
        if resp.status_code != 200:
            return {"error": "Failed to fetch location"}
        result = resp.json()
        if result.get("status") != "success":
            return {"error": "Invalid IP address"}
        return {
            "ip": result.get("query"),
            "country": result.get("country"),
            "region": result.get("regionName"),
            "city": result.get("city"),
            "isp": result.get("isp"),
            "lat": result.get("lat"),
            "lon": result.get("lon")
        }


@router.post("/lookup")
def lookup_ip(data: IPRequest):
    """Endpoint delegating to GeoService."""
    return GeoService().lookup(data.ip)