from bs4 import BeautifulSoup

def validate_response(response_html):
    return response_html.status_code == 200

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    
    extract_titles(soup)

def extract_titles(soup):
    elements = soup.select("article h2, div.wp-block-tc23-post-picker h2, h2.has-link-color wp-block-post-title wp-elements-bfa04303c7f1029d1f026872d399c7ae")
    for element in elements:
        title = element.get_text().strip()
        print(f"Title: {title}")