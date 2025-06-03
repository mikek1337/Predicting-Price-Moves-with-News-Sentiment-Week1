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
        """
        Loads price data from a CSV file specified by self.price_csv.

        The method reads the CSV file into a pandas DataFrame, converts the 'Date' column to UTC datetime,
        normalizes it to remove time information, and sets it as the DataFrame index. Raises a ValueError
        if the 'Date' column is missing.

        Raises:
            ValueError: If the price data does not contain a 'Date' column.
        """
        # Load price data
        self.price_data = pd.read_csv(self.price_csv)
        if 'Date' in self.price_data.columns:
            self.price_data['Date'] = pd.to_datetime(self.price_data['Date'], utc=True).dt.normalize()
            self.price_data.set_index('Date', inplace=True)
        else:
            raise ValueError("Price data must have a 'Date' column.")

    def align_data(self):
        """
        Aligns price data and daily sentiment data on the 'date' column.

        Joins the `price_data` DataFrame with the `daily_sentiment` DataFrame (after setting its index to 'date')
        using an inner join, ensuring that only dates present in both datasets are retained. 
        The result is stored in the `self.aligned` attribute.

        Handles AttributeError by printing the `daily_sentiment` DataFrame and an error message for debugging purposes.
        """
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
        """
        Calculates the daily return percentage for the 'Close' prices in the aligned DataFrame.

        The method computes the percentage change between consecutive 'Close' prices and stores the result
        in a new column 'daily_return' within the self.aligned DataFrame.

        Returns:
            None: The method updates the self.aligned DataFrame in place.
        """
        # Calculate daily returns in percent
        self.aligned['daily_return'] = self.aligned['Close'].pct_change() * 100

    def correlation_analysis(self, plot=True):
        """
        Performs correlation analysis between daily news sentiment (compound score) and stock daily returns.

        This method calculates the Pearson correlation coefficient between the 'compound' sentiment score and the 'daily_return' for the specified stock ticker. Optionally, it can generate a scatter plot visualizing the relationship between these two variables.

        Args:
            plot (bool, optional): If True, displays a scatter plot of sentiment vs. daily return. Defaults to True.

        Returns:
            float: The Pearson correlation coefficient between daily news sentiment and stock returns.

        Prints:
            The computed Pearson correlation value with a descriptive message.
        """
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
        """
        Executes the full data processing pipeline: loads data, aligns it, calculates daily returns, and performs correlation analysis.

        Args:
            plot (bool, optional): If True, generates plots during correlation analysis. Defaults to True.

        Returns:
            Any: The result of the correlation analysis, as returned by `self.correlation_analysis`.
        """
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

