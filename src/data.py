import pandas as pd
class Data:
    """A class for loading and accessing data from a CSV file.
    Attributes:
        data (pandas.DataFrame): The data loaded from the specified CSV file.
    Methods:
        load_data():"""
    def __init__(self, path:str):
        self.data = pd.read_csv(path)
    
    def load_data(self):
        """
        Returns the loaded dataset.

        Returns:
            Any: The data stored in the `self.data` attribute.
        """
        return self.data
        