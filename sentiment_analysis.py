from textblob import TextBlob


def analyze_sentiment(comments):
    """
    Performs sentiment analysis on a list of comments using TextBlob.

    Args:
        comments (list): A list of comment dictionaries containing text content.

    Returns:
        list: A list of sentiment polarity scores for each comment, ranging from -1 (negative) to 1 (positive).
    """

    sentiments = []
    for comment in comments:
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        sentiments.append(sentiment)

    return sentiments
