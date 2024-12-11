import requests

# API URL
url = "http://127.0.0.1:8000/myapi"

try:
    # Send a GET request to your API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse and display the response
        data = response.json()
        print("Response from your API:")
        print(data)
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
