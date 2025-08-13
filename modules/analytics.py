import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def extract_metrics(text):
    return {
        "word_count": len(text.split()),
        "keyword_hits": sum([text.lower().count(k) for k in ["python", "salesforce", "streamlit"]])
    }

def to_dataframe(metrics, feedback, match_result=None, version=None):
    data = {
        "Version": version or "v1",
        "Word Count": metrics["word_count"],
        "Keyword Hits": metrics["keyword_hits"],
        "Feedback": feedback
    }

    if match_result:
        data["Match Score"] = match_result["Match Score"]
        data["Missing Keywords"] = ", ".join(match_result["Missing Keywords"])

    return pd.DataFrame([data])

def plot_match_score_trend(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df["Version"], df["Match Score"], marker='o', color='teal')
    plt.title("Match Score Trend by Version")
    plt.xlabel("Version")
    plt.ylabel("Match Score")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("match_score_trend.png")
    plt.close()

def plot_missing_keyword_frequency(df):
    all_keywords = []
    for keywords in df["Missing Keywords"].dropna():
        all_keywords.extend(keywords.split(", "))

    keyword_counts = Counter(all_keywords)
    keywords, counts = zip(*keyword_counts.items())

    plt.figure(figsize=(8, 4))
    plt.bar(keywords, counts, color='salmon')
    plt.title("Missing Keyword Frequency")
    plt.xlabel("Keyword")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("missing_keyword_frequency.png")
    plt.close()
