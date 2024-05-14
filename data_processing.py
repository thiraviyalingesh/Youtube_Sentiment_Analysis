import pandas as pd
from youtube_api import get_comments  # Assuming youtube_api.py is in the same directory
from sentiment_analysis import analyze_sentiment


def process_data(videos, api_key):
    """
    Processes video data and performs sentiment analysis, returning a DataFrame.

    Args:
        videos (list): A list of video dictionaries containing details.

    Returns:
        pd.DataFrame: A DataFrame containing video titles, published times, total comments, and average sentiment.
    """

    data = []
    for video in videos:
        title = video['snippet']['title']
        published_at = video['snippet']['publishedAt']
        video_id = video['id']['videoId']

        comments = get_comments(video_id, api_key)
        sentiments = analyze_sentiment(comments)

        total_comments = len(comments)
        total_sentiment = sum(sentiments) if sentiments else 0
        average_sentiment = total_sentiment / total_comments if total_comments > 0 else 0

        data.append({
            'Title': title,
            'Published At': published_at,
            'Total Comments': total_comments,
            'Average Sentiment': average_sentiment
        })

    return pd.DataFrame(data)
