# Web Scraper for News Headlines
# Task 3 - Python Developer Internship

import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # Website URL
    url = "https://www.bbc.com/news"

    try:
        # Add headers (important to avoid blocking)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        # Send GET request
        response = requests.get(url, headers=headers)

        # Check status code
        if response.status_code != 200:
            print("Failed to fetch webpage. Status code:", response.status_code)
            return

        print("✅ Webpage fetched successfully")

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all headlines (BBC uses h3 tags)
        headlines = soup.find_all("h3")

        # Extract text from headlines
        news_titles = []

        for headline in headlines:
            text = headline.get_text().strip()
            if text and text not in news_titles:
                news_titles.append(text)

        # Save headlines to file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            file.write("Top News Headlines\n")
            file.write("===================\n\n")

            for i, title in enumerate(news_titles, start=1):
                file.write(f"{i}. {title}\n")

        print(f"✅ {len(news_titles)} headlines saved to headlines.txt")

    except Exception as e:
        print("❌ Error occurred:", e)


# Run the function
if __name__ == "__main__":
    scrape_headlines()
