# news_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and len(text) > 10 and text not in headlines:
            headlines.append(text)

    return headlines[:20]  # Get only top 20

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for idx, headline in enumerate(headlines, 1):
            file.write(f"{idx}. {headline}\n")
    print(f"Saved {len(headlines)} headlines to {filename}")

if __name__ == "__main__":
    news_url = "https://www.indiatoday.in/aajtak-livetv"
    headlines = fetch_headlines(news_url)
    save_to_file(headlines)
    
