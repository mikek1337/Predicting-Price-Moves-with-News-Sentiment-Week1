import numpy as np
import matplotlib.pyplot as plt
import talib as ta
import pandas as pd

class FinanicalAnalysis:
    """
    FinanicalAnalysis provides methods to compute common technical indicators on financial time series data.
    Attributes:
        df (pd.DataFrame): The input DataFrame containing financial data, indexed by 'Date'.
    Methods:
        calculate_RSI(timeperiod: int = 14):
            Calculates the Relative Strength Index (RSI) for the specified time period and adds it as a new column.
        calculate_SMA(timeperiod: int = 20):
            Calculates the Simple Moving Average (SMA) for the specified time period and adds it as a new column.
        calculate_EMA(timeperiod: int = 20):
            Calculates the Exponential Moving Average (EMA) for the specified time period and adds it as a new column.
        calculate_MACD():
            Calculates the Moving Average Convergence Divergence (MACD), MACD signal, and MACD histogram, adding them as new columns.
        calculate_daily_return():
            Calculates the daily percentage return of the 'Close' price and adds it as a new column.
        technical_indicators():
            Computes EMA, RSI, SMA, and MACD indicators and returns the updated DataFrame.
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('Date', inplace=True)

    def calculate_RSI(self, timeperiod:int = 14):
        """
        Calculates the Relative Strength Index (RSI) for the 'Close' prices in the DataFrame and adds it as a new column.

        Args:
            timeperiod (int, optional): The number of periods to use for calculating RSI. Defaults to 14.

        Returns:
            None: The method updates the DataFrame in place by adding a new column named 'RSI_<timeperiod>'.
        """
        self.df['RSI_'+str(timeperiod)] = ta.RSI(self.df['Close'], timeperiod=timeperiod)
    
    def calculate_SMA(self, timeperiod:int=20):
        """
        Calculates the Simple Moving Average (SMA) for the 'Close' price over a specified time period and adds it as a new column to the DataFrame.

        Args:
            timeperiod (int, optional): The number of periods to use for calculating the SMA. Defaults to 20.

        Returns:
            None: The method updates the DataFrame in place by adding a new column named 'SMA_<timeperiod>'.
        """
        self.df['SMA_'+str(timeperiod)] = ta.SMA(self.df['Close'], timeperiod=timeperiod)
    def calculate_EMA(self, timeperiod:int=20):
        """
        Calculates the Exponential Moving Average (EMA) for the 'Close' price column over a specified time period and adds it as a new column to the DataFrame.

        Args:
            timeperiod (int, optional): The number of periods to use for calculating the EMA. Defaults to 20.

        Returns:
            None: The method updates the DataFrame in place by adding a new column named 'EMA_<timeperiod>'.
        """
        self.df['EMA_'+str(timeperiod)] = ta.EMA(self.df['Close'], timeperiod=timeperiod)
    
    def calculate_MACD(self):
        """
        Calculates the Moving Average Convergence Divergence (MACD) indicator for the 'Close' prices in the DataFrame.

        This method adds three new columns to the DataFrame:
        - 'MACD': The MACD line, calculated as the difference between the 12-period and 26-period exponential moving averages.
        - 'MACD_signal': The signal line, which is a 9-period exponential moving average of the MACD line.
        - 'MACD_hist': The MACD histogram, representing the difference between the MACD line and the signal line.

        Requires the 'ta' (technical analysis) library.

        Returns:
            None
        """
        self.df['MACD'], self.df['MACD_signal'], self.df['MACD_hist'] = ta.MACD(
        self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    def calculate_daily_return(self):
        """
        Calculates the daily return percentage based on the 'Close' price and adds it as a new column 'daily_return' to the DataFrame.

        The daily return is computed as the percentage change between consecutive closing prices.
        """
        self.df['daily_return'] = self.df['Close'].pct_change() * 100
    
    def technical_indicators(self):
        """
        Calculates and appends multiple technical indicators to the DataFrame.

        This method sequentially computes the Exponential Moving Average (EMA),
        Relative Strength Index (RSI), Simple Moving Average (SMA), and
        Moving Average Convergence Divergence (MACD) for the dataset stored in
        `self.df`. The results of each indicator calculation are added as new
        columns to the DataFrame.

        Returns:
            pandas.DataFrame: The DataFrame with the newly added technical indicator columns.
        """
        self.calculate_EMA()
        self.calculate_RSI()
        self.calculate_SMA()
        self.calculate_MACD()
        return self.df;
    
    
