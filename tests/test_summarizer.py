import pytest
from app.summarizer import summarize_text

def test_summarize_valid_input():
    text = "The quick brown fox jumps over the lazy dog. " * 10  # 90+ words
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 20

def test_summarize_short_input():
    text = "Too short."
    result = summarize_text(text)
    assert result.lower().startswith("text too short")

def test_summarize_empty_input():
    text = ""
    result = summarize_text(text)
    assert "invalid" in result.lower() or "error" in result.lower()
