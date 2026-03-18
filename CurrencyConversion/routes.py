from fastapi import APIRouter
from models import CurrencyRequest
import requests

router = APIRouter()

API_KEY = "7aea5a8f4c72accf40c2fae2"  # 🔴 Replace this


class CurrencyService:

    BASE = "https://v6.exchangerate-api.com/v6"

    def convert(self, frm: str, to: str, amount: float):
        frm = frm.strip().upper()
        to = to.strip().upper()

        url = f"{self.BASE}/{API_KEY}/pair/{frm}/{to}/{amount}"
        print("URL:", url)

        try:
            resp = requests.get(url, timeout=10)
            data = resp.json()
        except Exception as e:
            return {"error": str(e)}

        print("RESPONSE:", data)

        if data.get("result") != "success":
            return {"error": "Conversion failed (check currency codes or API key)"}

        return {
            "from": frm,
            "to": to,
            "amount": amount,
            "converted_amount": data.get("conversion_result")
        }


@router.post("/convert")
def convert_currency(data: CurrencyRequest):
    svc = CurrencyService()
    return svc.convert(data.from_currency, data.to_currency, data.amount)