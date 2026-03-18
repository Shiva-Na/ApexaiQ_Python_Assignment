from pydantic import BaseModel


class CurrencyRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float