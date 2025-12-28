import re
from datetime import datetime

# -------------------------
# 1. Source credibility scores
# -------------------------
SOURCE_SCORES = {
    # ---------------------
    # Highly credible international sources
    # ---------------------
    "bbc.com": 9,
    "cnn.com": 8,
    "reuters.com": 9,
    "theguardian.com": 8,
    "nytimes.com": 9,
    "washingtonpost.com": 8,
    "aljazeera.com": 8,
    "apnews.com": 9,

    # ---------------------
    # North Indian credible sources
    # ---------------------
    "timesofindia.indiatimes.com": 9,
    "hindustantimes.com": 9,
    "thehindu.com": 9,
    "indianexpress.com": 8,
    "livemint.com": 8,
    "ndtv.com": 8,

    # ---------------------
    # South Indian credible sources
    # ---------------------
    "thehindu.com/tamil": 8,
    "eenadu.net": 8,
    "sakshi.com": 8,
    "manoramaonline.com": 8,
    "dinamalar.com": 7,
    "deccanherald.com": 8,

    # ---------------------
    # Moderate credibility / opinionated sources
    # ---------------------
    "huffpost.com": 6,
    "buzzfeednews.com": 6,
    "cnbc.com": 7,
    "foxnews.com": 6,
    "scroll.in": 7,
    "firstpost.com": 7,
    "news18.com": 7,

    # ---------------------
    # Low credibility / known fake-news sites
    # ---------------------
    "fake-news-site.xyz": 2,
    "unknownsource.com": 3,
    "infowars.com": 2,
    "beforeitsnews.com": 2,
    "worldnewsdailyreport.com": 1,
    "dailybuzzlive.com": 2,
    "opindia.com": 3,
    "indiaaheadnews.com": 2,
    "beyondheadlines.in": 2
}


def check_source(url):
    if not url:
        return 3, "No source URL provided"
    for source in SOURCE_SCORES:
        if source in url:
            return SOURCE_SCORES[source], None
    return 3, "Source is unknown or low credibility"

# -------------------------
# 2. Language pattern check
# -------------------------
SENSATIONAL_WORDS = [
    "shocking", "unbelievable", "breaking", "miracle", "you won't believe",
    "amazing", "incredible", "must see", "cannot believe", "scandal"
]

def check_language(text):
    for word in SENSATIONAL_WORDS:
        if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
            return False, f"Contains sensational word: '{word}'"
    return True, None

# -------------------------
# 3. Time check
# -------------------------
def check_time(article_date=None):
    if article_date:
        now = datetime.now()
        if article_date > now:
            return False, "Article date is in the future"
    return True, None

# -------------------------
# 4. Summarization
# -------------------------
def summarize_content(content, sentence_count=3):
    sentences = [s.strip() for s in re.split(r'[.!?]', content) if s.strip()]
    summary = ". ".join(sentences[:sentence_count])
    if summary:
        summary += "."
    return summary

# -------------------------
# 5. Evaluate credibility
# -------------------------
def evaluate_credibility(content, url=None, article_date=None):
    score = 10
    reasons = []

    # Source
    if url:
        s_score, s_reason = check_source(url)
        score = min(score, s_score)
        if s_reason:
            reasons.append(s_reason)
    
    # Language
    lang_ok, lang_reason = check_language(content)
    if not lang_ok:
        score = min(score, 4)
        reasons.append(lang_reason)

    # Time
    time_ok, time_reason = check_time(article_date)
    if not time_ok:
        score = min(score, 5)
        reasons.append(time_reason)

    # Summary
    summary = summarize_content(content)

    return score, reasons, summary

# -------------------------
# Example test
# -------------------------
if __name__ == "__main__":
    test_content = "Breaking news! Something unbelievable happened!"
    test_url = "https://fake-news-site.xyz/article"
    score, reasons, summary = evaluate_credibility(test_content, test_url)
    print("Credibility Score:", score)
    print("Reasons:", reasons)
    print("Summary:", summary)
