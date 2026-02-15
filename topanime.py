import urllib3
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url = "https://www.imdb.com/search/title/?keywords=anime"

http = urllib3.PoolManager()

try:
    response = http.request('GET', url, headers=headers)
    soup = BeautifulSoup(response.data, "lxml")

    # 1. Find the list of all movie cards (usually 'li' tags in the new layout)
    anime_cards = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    
    for card in anime_cards[:10]:  # Get top 10 anime
    # 2. Extract the Title (handling cases where it might be missing)
        title_element = card.find('h3', class_='ipc-title__text')
        title = title_element.text if title_element else "Unknown Title"

    # 3. Extract the Rating
    # We look for the span with the specific rating class
        rating_element = card.find('span', class_='ipc-rating-star--rating')
        rating = rating_element.text if rating_element else "N/A"
        
        print(f"{title} | Rating: {rating}")

except Exception as e:
    print(f"An error occurred: {e}")
    

