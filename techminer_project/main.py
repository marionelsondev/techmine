import requests
from bs4 import BeautifulSoup
url = "https://techcrunch.com/"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
    print("Successful request")
    soup = BeautifulSoup(html_content, 'lxml')
    print(soup.prettify())
else:
    print("Request failed")