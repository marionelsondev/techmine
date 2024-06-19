import requests
from code_utils.utils import *

url = "https://techcrunch.com/"

# Making the HTTP request to the requested url
response = requests.get(url)

# Function to check the server response, if successful the script will extract the desired data
validate_extract(response)