from fastapi import FastAPI,Request
from pydantic import BaseModel
from app.summarizer import summarize_text
from app.news_fetcher import fetch_top_headlines
from app.classifier import classify_news
from app.utils import extract_article_text


app = FastAPI()

class TextInput(BaseModel):
    text : str

@app.get("/top-news")
def top_news(niche:str=None):
    articles = fetch_top_headlines()
    results = []

    for article in articles:
        news = extract_article_text(article["url"])
        if not news or "Error" in news or "not enough" in news.lower():
            continue
        summary = summarize_text(news)
        if summary.startswith("Error"):
            continue
        category = classify_news(summary)

        if not niche or niche.lower() == category:
            results.append({
                "title": article["title"],
                "url": article['url'],
                "summary":summary,
                "niche":category
            })
        
    return results

