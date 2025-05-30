import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
nltk.download('stopwords')
nltk.download('punkt_tab')
class TopicModeling:
    """
    A class for performing topic modeling on a pandas DataFrame column using Latent Dirichlet Allocation (LDA).
    Attributes:
        stopwords (set): Set of English stopwords used for text preprocessing.
        col (pd.DataFrame): The DataFrame column containing text data to be modeled.
        vectorize (CountVectorizer): The vectorizer instance for converting text to a document-term matrix.
    Methods:
        remove_stopwords(text):
            Removes stopwords and non-alphabetic tokens from the input text.
            Args:
                text (str): The input text to process.
            Returns:
                str: The processed text with stopwords removed.
        create_vector(min_occurrence: int, max_occurence: int):
            Creates a CountVectorizer with specified minimum and maximum document frequency.
            Args:
                min_occurrence (int): Minimum number of documents a word must appear in.
                max_occurence (int): Maximum number of documents a word can appear in (as a percentage).
            Returns:
                CountVectorizer: The configured vectorizer.
        fit_model():
            Fits an LDA model to the processed text data.
            Returns:
                LatentDirichletAllocation: The fitted LDA model.
        print_topics(model: LatentDirichletAllocation, n_top_words: int):
            Prints the top words for each topic in the fitted LDA model.
            Args:
                model (LatentDirichletAllocation): The trained LDA model.
                n_top_words (int): Number of top words to display for each topic.
    """
    def __init__(self, col:pd.DataFrame):
        self.stopwords = set(stopwords.words('english'))
        self.col = col
        self.vectorize = self.create_vector(2, 95)

    def remove_stopwords(self,text):
        """
        Removes stopwords and non-alphabetic tokens from the input text.

        Tokenizes the input text, filters out tokens that are not purely alphabetic,
        and excludes any tokens that are present in the instance's stopwords set.

        Args:
            text (str): The input text to process.

        Returns:
            str: The processed text with stopwords and non-alphabetic tokens removed.
        """
        tokens = word_tokenize(text)
        return ' '. join([word for word in tokens if word.isalpha() and word not in self.stopwords])
    
    
    def create_vector(self, min_occurrence:int, max_occurence:int):
        """
        Creates and returns a CountVectorizer instance with specified minimum and maximum document frequency thresholds.

        Args:
            min_occurrence (int): Minimum number of documents a term must appear in to be included in the vocabulary (min_df).
            max_occurence (int): Maximum number of documents a term can appear in to be included in the vocabulary (max_df).

        Returns:
            CountVectorizer: An instance of sklearn's CountVectorizer configured with the given parameters.
        """
        return CountVectorizer(max_df=max_occurence, min_df=min_occurrence)
        

    def fit_model(self):
        """
        Fits a Latent Dirichlet Allocation (LDA) topic model to the processed text data.

        This method processes the text data by removing stopwords, vectorizes the processed text using the
        provided vectorizer, and then fits an LDA model with a specified number of topics.

        Returns:
            LatentDirichletAllocation: The fitted LDA model.
        """
        processed_frame = self.col.apply(self.remove_stopwords)
        df_matrix = self.vectorize.fit_transform(processed_frame)
        lda = LatentDirichletAllocation(n_components=5, random_state=42)
        lda.fit(df_matrix)
        return lda


    def print_topics(self, model:LatentDirichletAllocation, n_top_words:int):
        """
        Prints the top words for each topic in a fitted Latent Dirichlet Allocation (LDA) model.

        Args:
            model (LatentDirichletAllocation): The fitted LDA model whose topics are to be displayed.
            n_top_words (int): The number of top words to display for each topic.

        Returns:
            None

        Side Effects:
            Prints the top words for each topic to the standard output.
        """
        feature_names = self.vectorize.get_feature_names_out() 
        for topic_idx, topic in enumerate(model.components_):
            print(f"Topic #{topic_idx + 1}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            print()
