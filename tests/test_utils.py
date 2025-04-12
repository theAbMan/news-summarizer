from app.utils import extract_article_text

def test_extract_invalid_url():
    text = extract_article_text("https://nonexistent-url.fake/news")
    assert "error" in text.lower()

def test_extract_non_article_page():
    text = extract_article_text("https://www.google.com")
    assert "not enough" in text.lower() or "error" in text.lower()