from googleapiclient.discovery import build
from datetime import datetime, timedelta
from httplib2 import HttpError
from googleapiclient.errors import HttpError



def search_videos(query, start_date, end_date, api_key):
    """
    Retrieves videos based on a search query and date range using the YouTube Data API v3.

    Args:
        query (str): The search query for videos.
        start_date (datetime): The start date for the search range (inclusive).
        end_date (datetime): The end date for the search range (exclusive).
        api_key (str): Your YouTube Data API key.

    Returns:
        list: A list of video dictionaries containing details from the API response.
    """

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        type='video',
        q=query,
        publishedAfter=start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
        publishedBefore=(end_date + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        maxResults=10000  # Adjust as needed
    )

    response = request.execute()
    return response['items']


# def get_comments(video_id, api_key, max_results=1000000):
#     """
#     Retrieves comments for a given video ID using the YouTube Data API v3.

#     Args:
#         video_id (str): The ID of the video for which to retrieve comments.
#         api_key (str): Your YouTube Data API key.
#         max_results (int, optional): The maximum number of comments to retrieve. Defaults to 1000000.

#     Returns:
#         list: A list of comment dictionaries containing details from the API response.
#     """

#     youtube = build('youtube', 'v3', developerKey=api_key)

#     comments_request = youtube.commentThreads().list(
#         part='snippet',
#         videoId=video_id,
#         textFormat='plainText',
#         maxResults=max_results
#     )

#     comments_response = comments_request.execute()
#     return comments_response['items']

def get_comments(video_id, api_key, max_results=1000000):
    """
    Retrieves comments for a given video ID using the YouTube Data API v3.

    Args:
        video_id (str): The ID of the video for which to retrieve comments.
        api_key (str): Your YouTube Data API key.
        max_results (int, optional): The maximum number of comments to retrieve. Defaults to 1000000.

    Returns:
        list: A list of comment dictionaries containing details from the API response (empty if comments are disabled).
    """

    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        comments_request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=max_results
        )
        comments_response = comments_request.execute()
        return comments_response['items']

    except HttpError as error:
        if error.resp.status == 403:  # Check for comments disabled error
            # Handle the case where comments are disabled
            print(f"Comments are disabled for video: {video_id}")
            return []  # Return an empty list
        else:
            # Raise other unexpected errors
            raise error
