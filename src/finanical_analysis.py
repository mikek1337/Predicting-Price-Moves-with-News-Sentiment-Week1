import numpy as np
import matplotlib.pyplot as plt
import talib as ta
import pandas as pd

class FinanicalAnalysis:
    def __init__(self, df:pd.DataFrame):
        self.df = df
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('Date', inplace=True)

    def calculate_RSI(self, timeperiod:int = 14):
        self.df['RSI_'+timeperiod] = ta.RSI(self.df['Close'], timeperiod=timeperiod)
    
    def calculate_SMA(self, timeperiod:int=20):
        self.df['SMA_'+timeperiod] = ta.SMA(self.df['Close'], timeperiod=timeperiod)
    def calculate_EMA(self, timeperiod:int=20):
        self.df['EMA_'+timeperiod] = ta.EMA(self.df['Close'], timeperiod=timeperiod)
    
    def calculate_MACD(self, timeperiod):
        self.df['MACD'], self.df['MACD_signal'], self.df['MACD_hist'] = ta.MACD(
        self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    def calculate_daily_return(self):
        self.df['daily_return'] = self.df['Close'].pct_change() * 100
    
    
