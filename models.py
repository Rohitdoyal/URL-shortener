from pydantic import BaseModel, Field
from typing import Optional

class URLRequest(BaseModel):
    long_url: str
    ttl: Optional[int] = Field(None, description="Time-to-live in seconds (optional)")

class URLResponse(BaseModel):
    short_url: str

class StatsResponse(BaseModel):
    short_url: str
    access_count: int
