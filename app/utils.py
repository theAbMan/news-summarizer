import requests
from bs4 import BeautifulSoup
from newspaper import Article
from readability import Document


def extract_article_text(url: str) -> str:
    try:
        # First try with newspaper
        article = Article(url)
        article.download()
        article.set_html(article.html)
        article.config.browser_user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        )
        article.parse()

        text = article.text.strip()
        if text and len(text.split()) > 30:
            return text
    except Exception as e:
        print(f"[WARN] Newspaper3k failed for {url}: {e}")

    # Fallback: use readability + requests + soup
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/112.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        doc = Document(response.text)
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, "lxml")
        fallback_text = soup.get_text(separator="\n").strip()

        if fallback_text and len(fallback_text.split()) > 30:
            return fallback_text
        else:
            return "Not enough content to summarize."
    except Exception as e:
        print(f"[ERROR] Readability fallback also failed for {url}: {e}")
        return "Error: Failed to extract article"
