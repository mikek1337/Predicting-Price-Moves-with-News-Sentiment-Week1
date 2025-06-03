import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
class Sentiment:
    """
    A class for analyzing news sentiment related to stock tickers using VADER sentiment analysis.
    Attributes:
        news_data (pd.DataFrame): DataFrame containing news headlines and associated metadata.
        daily_sentiment (pd.DataFrame): DataFrame containing aggregated daily sentiment scores for a given ticker.
    Methods:
        __init__(headlines_csv: str):
            Initializes the Sentiment object by loading news data from a CSV file and parsing the 'date' column.
        compute_sentiment(ticker: str) -> pd.DataFrame:
            Computes sentiment scores for news headlines if not already present, filters news for the specified ticker,
            and aggregates sentiment scores by date. Returns a DataFrame with daily sentiment scores.
    """
    def __init__(self, headlines_csv:str):
        self.news_data = pd.read_csv(headlines_csv)
        
        self.news_data['date'] = pd.to_datetime(self.news_data['date'], format='mixed', utc=True) 

    def compute_sentiment(self, ticker:str):
        # Compute sentiment scores if not already present
        if not {'neg', 'neu', 'pos', 'compound'}.issubset(self.news_data.columns):
            vader = SentimentIntensityAnalyzer()
            scores = [vader.polarity_scores(str(headline)) for headline in self.news_data['headline'].values]
            scores_df = pd.DataFrame(scores)
            self.news_data = pd.concat([self.news_data, scores_df], axis=1)

        # Aggregate sentiment by day for the given ticker
        ticker_news = self.news_data[self.news_data['stock'].str.upper() == ticker]
        print(ticker_news.head())
        self.daily_sentiment = ticker_news.groupby('date')[['neg', 'neu', 'pos', 'compound']].mean().reset_index()
        return self.daily_sentiment
    