from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta

from models import URLRequest, URLResponse, StatsResponse
from utils import generate_short_url, is_valid_url
from storage import storage, access_stats


app = FastAPI()
# Base URL for the shortener
BASE_URL = "http://localhost:8000/" 

@app.post("/shorten", response_model=URLResponse)
def shorten_url(url_request: URLRequest):
    long_url = url_request.long_url
    ttl = url_request.ttl

    if not is_valid_url(long_url):
        raise HTTPException(status_code=400, detail="Invalid url")

    if long_url in storage['long_to_short']:
        # print("long url already exist")
        short_url = storage['long_to_short'][long_url]

    else:
        short_url = generate_short_url(long_url)
        storage['long_to_short'][long_url] = short_url
        storage['short_to_long'][short_url] = {
            "long_url": long_url,
            "expires_at": datetime.now() + timedelta(seconds=ttl) if ttl else None
        }
        access_stats[short_url] = 1

    return URLResponse(short_url=BASE_URL + short_url)



@app.get("/{short_url}")
def redirect_to_long_url(short_url: str):
    if short_url not in storage['short_to_long']:
        raise HTTPException(status_code=404, detail="Short URL not found")

    url_data = storage['short_to_long'][short_url]
    
    # url is expire or not 
    if url_data['expires_at'] and datetime.now() > url_data['expires_at']:
        del storage['short_to_long'][short_url]
        del storage['long_to_short'][url_data['long_url']]
        del access_stats[short_url]
        raise HTTPException(status_code=410, detail="Short URL has been expired")

    # update status number of times url access 
    access_stats[short_url] = access_stats[short_url]+1
    return RedirectResponse(url=url_data['long_url'])


@app.get("/stats/{short_url}", response_model=StatsResponse)
def get_stats(short_url: str):
    # if we want to check number of time short url access. 
    if short_url not in access_stats:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    return StatsResponse(
        short_url=BASE_URL + short_url,
        access_count=access_stats[short_url]
    )
