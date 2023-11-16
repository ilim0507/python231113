import requests
from bs4 import BeautifulSoup

def crawl_inven_page(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information
        articles = []
        for article in soup.find_all('tr', class_='lgtm'):
            type = article.find('span', class_='category').text.strip()
            title = article.find('a', class_='subject-link').text.strip().replace("\n", "")
            writer = article.find('span', class_='layerNickName').text.strip()
            date = article.find('td', class_='date').text.strip()
            articles.append({
                'type': type,
                'title': title,
                'writer': writer,
                'date': date
            })

        return articles
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")
        return None

# URL of the page to crawl
url = 'https://www.inven.co.kr/board/lostark/4821?p=2'

# Call the function and print the result
result = crawl_inven_page(url)
if result:
    for article in result:
        print(article)