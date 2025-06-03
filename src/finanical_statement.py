import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FinancialSentimentAnalyzer:
    """
    FinancialSentimentAnalyzer analyzes the relationship between daily news sentiment and stock price movements for a given ticker.

    Attributes:
        ticker (str): The stock ticker symbol (in uppercase).
        price_csv (str): Path to the CSV file containing historical price data.
        daily_sentiment (pd.DataFrame): DataFrame containing daily sentiment scores with a 'date' column.
        price_data (pd.DataFrame or None): DataFrame containing loaded price data.
        aligned (pd.DataFrame or None): DataFrame with price and sentiment data aligned by date.

    Methods:
        load_data():
            Loads historical price data from the specified CSV file, parses the 'Date' column, and sets it as the index.

        align_data():
            Aligns the loaded price data with the sentiment DataFrame on the date index, keeping only matching dates.

        calculate_daily_return():
            Calculates the daily percentage return of the stock and adds it as a new column 'daily_return' to the aligned DataFrame.

        correlation_analysis(plot=True):
            Computes and prints the Pearson correlation between daily sentiment (compound score) and daily stock returns.
            Optionally plots a scatter plot of sentiment vs. returns.

        run_all(plot=True):
            Runs the full analysis pipeline: loads data, aligns data, calculates daily returns, and performs correlation analysis.
            Returns the computed correlation coefficient.
    """
    def __init__(self, price_csv:str, sentiment:pd.DataFrame, ticker:str):
        self.ticker = ticker.upper()
        self.price_csv = price_csv
        self.daily_sentiment = sentiment
        self.price_data = None
        self.aligned = None

    def load_data(self):
        # Load price data
        self.price_data = pd.read_csv(self.price_csv)
        if 'Date' in self.price_data.columns:
            self.price_data['Date'] = pd.to_datetime(self.price_data['Date'], utc=True).dt.normalize()
            self.price_data.set_index('Date', inplace=True)
        else:
            raise ValueError("Price data must have a 'Date' column.")

    def align_data(self):
        # Align price and sentiment data on date
        try:
            self.aligned = self.price_data.join(
                self.daily_sentiment.set_index('date'),
                how='inner'
            )
        except AttributeError:
            print(self.daily_sentiment)
            print('error occurred')

    def calculate_daily_return(self):
        # Calculate daily returns in percent
        self.aligned['daily_return'] = self.aligned['Close'].pct_change() * 100

    def correlation_analysis(self, plot=True):
        # Drop NA values for correlation
        corr_data = self.aligned[['daily_return', 'compound']].dropna()
        correlation = corr_data['daily_return'].corr(corr_data['compound'])
        print(f"Pearson correlation between daily news sentiment (compound) and {self.ticker} stock returns: {correlation:.4f}")

        if plot:
            plt.figure(figsize=(8,5))
            plt.scatter(corr_data['compound'], corr_data['daily_return'], alpha=0.5)
            plt.xlabel('Daily News Sentiment (Compound Score)')
            plt.ylabel(f'{self.ticker} Daily Return (%)')
            plt.title(f'Correlation between News Sentiment and {self.ticker} Stock Returns')
            plt.grid(True)
            plt.show()
        return correlation

    def run_all(self, plot=True):
        self.load_data()
        self.align_data()
        self.calculate_daily_return()
        return self.correlation_analysis(plot=plot)

# Example usage:
# analyzer = FinancialSentimentAnalyzer(
#     price_csv='../data/yfinance_data/AAPL_historical_data.csv',
#     sentiement=sentiment_data,
#     ticker='AAPL'
# )
# analyzer.run_all()

