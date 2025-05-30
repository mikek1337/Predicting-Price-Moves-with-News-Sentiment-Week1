# Predicting Price Moves with News Sentiment - Week 1

## Overview

This project explores the relationship between news article sentiment, publication trends, technical indicators, and potential price movements in financial markets. The primary focus for Week 1 is on data exploration, publication trend analysis, topic modeling of financial news headlines, and technical analysis of stock price data using TA-Lib.

## What Has Been Done

### 1. Data Loading and Preprocessing
- Loaded raw analyst ratings, news headline data, and historical stock price data from CSV files.
- Converted date columns to proper datetime format for time-series analysis.
- Checked for missing values and performed basic data cleaning.

### 2. Exploratory Data Analysis (EDA)
- Analyzed the distribution of article publication dates.
- Counted and visualized the number of articles published by each publisher.
- Calculated headline lengths for further text analysis.

### 3. Publication Trend Analysis
- Grouped articles by date (daily and monthly) and visualized the publication frequency over time using line plots.
- Identified trends and spikes in publication activity, which may correspond to significant market events.

### 4. Topic Modeling
- Preprocessed headlines by removing stopwords and tokenizing the text.
- Used `CountVectorizer` to convert processed headlines into a document-term matrix.
- Applied Latent Dirichlet Allocation (LDA) to extract topics from the headlines.
- Displayed the top words for each topic to interpret the main themes in the news data.
- Assigned each article to its most likely topic.

### 5. Topic Publication Frequency Over Time
- Grouped articles by both date and topic to analyze how the frequency of each topic changes over time.
- Visualized these trends with time-series plots, allowing for comparison between different topics.

### 6. Technical Analysis with TA-Lib
- Loaded historical stock price data (e.g., AAPL).
- Calculated technical indicators using TA-Lib:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Visualized the close price with SMA and EMA, RSI, and MACD to support financial analysis.

## Notebooks and Scripts

- **notebooks/publication-analysis.ipynb**: Main notebook containing all data exploration, trend analysis, and topic modeling steps.
- **notebooks/financial-analysis.ipynb**: Notebook for technical analysis of stock price data using TA-Lib indicators.
- **src/topic_modeling.py**: Python module encapsulating the topic modeling logic, including preprocessing, vectorization, and LDA fitting.
- **tests/test_topic_modeling.py**: Unit tests for the topic modeling module.

## How to Run

1. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the Jupyter notebooks:
    ```bash
    jupyter notebook notebooks/publication-analysis.ipynb
    jupyter notebook notebooks/financial-analysis.ipynb
    ```
3. To run tests:
    ```bash
    python -m unittest discover tests
    ```

## Next Steps

- Incorporate sentiment analysis of headlines.
- Correlate publication trends, topics, and technical indicators with actual price movements.
- Explore more advanced modeling techniques for prediction.
- Analyze intra-day publishing patterns for more granular trading insights.

---

**Author:**  
*mikek1337*  
*Date: May 2025*