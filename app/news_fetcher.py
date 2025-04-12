import requests
import os
from dotenv import load_dotenv
load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def fetch_top_headlines():
    url = (
        f"https://newsapi.org/v2/top-headlines?country=us&pageSize=15&apiKey={NEWSAPI_KEY}"
    )

    response = requests.get(url)
    articles = response.json().get("articles",[])
    print("📰 Raw NewsAPI articles:", articles)
    return [
        {
        "title": a['title'],
        "content": a['content'] or a['description'] or "",
        "url":a['url']      
    }
    for a in articles if a['content']]


if __name__ == "__main__":
    news = fetch_top_headlines()
    print(news[0]['content'])
