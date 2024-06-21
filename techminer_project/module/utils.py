from bs4 import BeautifulSoup

# Check the server response

def validate_response(response_html):
    return response_html.status_code == 200

# Extract the HTML from the URL

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    extract_news(soup)

# Extract the selected data such as news titles and links

def extract_news(soup):
    elements = soup.select("div.wp-block-tc23-post-picker h2 a")

    for element in elements:
        title = element.get_text().strip()

        link = element["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")