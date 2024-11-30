import requests

# Base URL of the FastAPI application
BASE_API_URL = "http://localhost:8000"

def shorten_url(long_url, ttl=None):
    # Send a Request to the API to Shorten a url.
    payload = {"long_url": long_url, "ttl": ttl}
    response = requests.post(f"{BASE_API_URL}/shorten", json=payload)
    if response.status_code == 200:
        print(f"Short URL: {response.json()['short_url']}")
        return response.json()['short_url']
    else:
        print(f"Error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")

def redirect_to_long_url(short_url):
    # test redirection by accessing the short url
    short_path = short_url.replace(BASE_API_URL + "/", "")
    response = requests.get(f"{BASE_API_URL}/{short_path}", allow_redirects=False)
    if response.status_code == 307:  # HTTP status for temporary redirect
        print(f"Redirected to: {response.headers['Location']}")
    else:
        print(f"Error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")

def get_stats(short_url):
    # Get stats for a short url
    short_path = short_url.replace(BASE_API_URL + "/", "")
    response = requests.get(f"{BASE_API_URL}/stats/{short_path}")
    if response.status_code == 200:
        stats = response.json()
        print(f"Short URL: {stats['short_url']}")
        print(f"Access Count: {stats['access_count']}")
    else:
        print(f"Error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")

def main():
    print("Hello, Welcome to the URL Shortener API Tester!")
    print("1. Shorten a Long URL")
    print("2. Check Stats for a Short URL and Test Redirection with a Short URL")
    print("3. Check Stats for a Short URL")
    print("4: Terminate the program")

    c = True
    while(c):
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                long_url = input("Enter the long URL: ")
                ttl = input("Enter the TTL in seconds (leave empty for no TTL): ")
                ttl = int(ttl) if ttl.strip() else None
                shorten_url(long_url, ttl)

            elif choice == 2:
                short_url = input("Enter the short URL: ")
                get_stats(short_url)
                redirect_to_long_url(short_url)

            elif choice == 2:
                short_url = input("Enter the short URL: ")
                get_stats(short_url)
                redirect_to_long_url(short_url)

            elif choice == 3:
                short_url = input("Enter the short URL: ")
                print("we are checking number of times this url got access")
                get_stats(short_url)
       
            elif choice == 4:
                c= False
                print("----- Program terminate-----")
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
            
            print("---------------------")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == "__main__":
    main()
