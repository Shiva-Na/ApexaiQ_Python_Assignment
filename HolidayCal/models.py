from pydantic import BaseModel


class HolidayRequest(BaseModel):
    country: str
    year: int