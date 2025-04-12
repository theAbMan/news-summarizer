
def classify_news(summary:str)->str:
    keywords = {
        "Technology": ["AI", "tech", "software", "robot", "startup"],
        "sports": ["match", "team", "player", "score", "tournament"],
        "politics": ["election", "government","minister", "policy"],
        "business": ["market","stocks", "startup", "fund","deal"],
        "health": ["covid", "vaccine", "hospital", "health"],
        "entertainment": ["movie", "film","actor","celebrity","music"]
    }

    for niche, keys in keywords.items():
        if any(word.lower() in summary.lower() for word in keys):
            return niche
    return "general"