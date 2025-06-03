import pandas as pd
class Data:
    def __init__(self, path:str):
        self.data = pd.read_csv(path)
    
    def load_data(self):
        return self.data
        