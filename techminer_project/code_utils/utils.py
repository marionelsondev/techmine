from bs4 import BeautifulSoup

def validate_extract(response_html):
    if response_html.status_code == 200:
        html_content = response_html.content
        print("Successful request")
        
        soup = BeautifulSoup(html_content, 'lxml')
        
        articles = soup.find_all("article")

        for article in articles:
            title_element = article.find("h2")
            if title_element:
                title = title_element.get_text().strip() 
                print(f"Title: {title}")

        main_new = soup.find_all("div", class_="wp-block-tc23-post-picker")

        for new in main_new:
            title_element = new.find("h2", class_="has-link-color wp-block-post-title wp-elements-bfa04303c7f1029d1f026872d399c7ae")
            if title_element:
                title = title_element.get_text().strip()
                print(f"Main title: {title}")
    else:
        print("Request failed")