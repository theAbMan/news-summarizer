from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    try:
        if not text or not isinstance(text, str):
            return "Invalid input: empty or non-text"

        text = text.strip().replace('\n', ' ')
        word_count = len(text.split())

        if word_count < 30:
            return "Text too short to summarize"

        # DistilBART safe zone ≈ 1024 tokens, we take 500 words max
        if word_count > 500:
            text = ' '.join(text.split()[:500])

        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    except Exception as e:
        print(f"[CUDA Crash] Text:\n{text[:200]}...\nError: {e}")
        return "Error while summarizing"