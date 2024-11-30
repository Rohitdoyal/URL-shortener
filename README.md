# URL Shortner Application 
1. This Application shorten long URLs and generate unique short URLs .
2. It's redirect the short url to original long url 
3. If we want we can also expire time for short url
4. Track url access count status. 

#  DESIGN AND APPROACH 
1. Framework : Fast API (it's speed , simplicity and Python based Framework)
2. Storage : In-memory storage is used to keep the implementation lightweight as mention in assignment.
3. For generating a short url i used hashlib.md5 function it's generate unique short URLs using the input URL,I     used 7 character length in short url. 
Exapainatin for using 7 character length : 
  a. so for creating a short url we can use a-z letter ,A-Z letter, Number 0-9 so total we have around 62 character 
  b. Now what should be the minimum length of short url for that let's have some calculation 
        length of short url       total possiable url
        (i).  1              :  62
        (ii). 2              : 62^2 = 3844
        (iii).3              : 64^3 = 262144
        ..
        (vi). 6              : 64^6 = 56 billion
        (vii).7              : 64^7 = 3.5 trillion     

  c. Now suppose in production 1000 url is generated persecond then 
     each year number of url we have: 1000*60*60*24*365 = 31.5 billion

  d. So if we building our application and per year it will generate 31.5 billion url so 6 charater will crate issue in 2 year that why i used 7 beacuse in 7 character we can create total 3.5 trillion short urls which is sufficient        

4. TTL Support: URLs can have an optional expiration time , Expired URLs are removed dynamically upon access.


# For Run the application:
Create Python Virtual Environment
python -m venv ./myenv 

## Activate the virtual environment 
.\myenv\Scripts\activate

## Required packages
1. fastapi
2. uvicorn
3. validators
4. requests

pip install fastapi, uvicorn, validators, requests

## Start the API 
uvicorn app:app --reload


## APIs
1. shorten url          :  POST Request : http://localhost:8000/shorten , payload WHERE  payload = {"long_url": long_url, "ttl": ttl}
2. redirect_to_long_url :  GET Request  : http://localhost:8000/{short_path}
3. get_stats_api_access :  GET Request : http://localhost:8000/stats/{short_path}

## API END POINT
1. Shorten URL  
 POST : 'http://localhost:8000/shorten'
 Request: { "long_url": "http://example.com", "ttl": 3600 }
 Response: { "short_url": "http://localhost:8000/abc123" }

2. Redirect Short url   
 GET : http://localhost:8000/{short_url}
  Response: Redirects to the original URL.

3. Access Statistics  
 GET : http://localhost:8000/stats/{short_url}
 Response: { "short_url": "http://localhost:8000/abc123", "access_count": 2 }




# For Test the api 
I write another script in test folder testapi.py
In this file i wrote function where i am calling the api 

so just run this script 
python testapi.py


# Challenge faced:
1.  handling the expire : once url is expire our logic dynamically check expiration and remove expired entries.
2.  testing : storge i used inmemory so while testing if api restart so it's remove older data. for keep it consistence i write python script to test the api and in that i call api in while loop, also invalid url and expire link require good testing .   