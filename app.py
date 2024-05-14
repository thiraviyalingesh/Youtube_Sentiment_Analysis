import streamlit as st
from youtube_api import search_videos
from sentiment_analysis import analyze_sentiment
from data_processing import process_data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# YouTube API key (replace with yours)
API_KEY = 'AIzaSyB42utn8N9iG071chI9c_7saEJqRIXVGHA'  # Replace with your actual YouTube Data API key


def main():
    st.title('YouTube Comment Sentiment Analysis')

    # User input for search query and date filters
    search_query = st.text_input('Enter search query:', '')
    start_date = st.date_input('Start date', datetime.today() - timedelta(days=30))
    end_date = st.date_input('End date', datetime.today())

    if st.button('Search'):
        if search_query:
            videos = search_videos(search_query, start_date, end_date, API_KEY)
            df = process_data(videos, API_KEY)

            # Display DataFrame in Streamlit
            st.write(df)

            # Overall sentiment analysis
            overall_sentiment = df['Average Sentiment'].mean()

            # Display pie chart of sentiment analysis
            fig, ax = plt.subplots()
            ax.pie([overall_sentiment, 1 - overall_sentiment], labels=['Positive', 'Negative'], autopct='%1.1f%%', startangle=90)
            ax.set_title('Overall Sentiment Analysis')
            ax.axis('equal')
            st.pyplot(fig)

        else:
            st.warning('Please enter a search query.')

if __name__ == '__main__':
    main()
