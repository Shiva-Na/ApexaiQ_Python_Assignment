from fastapi import APIRouter
from models import CryptoRequest
import requests

router = APIRouter()

class CryptoService:
    """Retrieve crypto prices from CoinGecko."""
    API_URL = "https://api.coingecko.com/api/v3/simple/price"

    def get_price(self, coin: str, currency: str):
        resp = requests.get(f"{self.API_URL}?ids={coin}&vs_currencies={currency}")
        if resp.status_code != 200:
            return {"error": "Failed to fetch crypto price"}
        data = resp.json()
        if coin not in data:
            return {"error": "Coin not found"}
        return {"coin": coin, "currency": currency, "price": data[coin][currency]}


@router.post("/price")
def get_crypto_price(data: CryptoRequest):
    """Endpoint delegating to CryptoService."""
    svc = CryptoService()
    return svc.get_price(data.coin.lower(), data.currency.lower())