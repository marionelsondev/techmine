import requests
from module.utils import *

url = "https://techcrunch.com/"

# Making the HTTP request to the requested url
response = requests.get(url)

# Condition to check the server response and extract the desired data
if validate_response(response):
    print("Successful request")
    extract_data(response.content)
else:
    print("Request failed")