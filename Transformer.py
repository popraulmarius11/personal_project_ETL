import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
class Transformer:
    def __init__(self,numeric,open_df=None,clasa=None,tip=None,scoala=None):
        self.numeric=numeric
        self.open_df=open_df
        self.clasa=clasa
        self.tip=tip
        self.scoala=scoala


    def aggregate_answers(self):
        '''
        '''
        # Extract unique questions
        questions = self.numeric["Intrebare"].unique()

        # Create array for storing values
        valori = np.zeros((len(questions), 5), dtype=int)

        # Iterate over rows and update array with response values
        k = -1
        j = 0
        for i in questions:
            k += 1
            while j < len(self.numeric["Intrebare"]) and i == self.numeric["Intrebare"][j]:
                valori[k][int(self.numeric["Raspuns"][j]) - 1] += 1
                j += 1

        # Create arrays for each column
        values = [1, 2, 3, 4, 5]
        values = values * len(questions)
        questions = np.repeat(questions, 5, axis=None)
        valori = valori.reshape(-1)

        # Create dataframe from arrays
        df = {"Intrebari": questions, "Raspuns": values, "Numar": valori}
        self.numeric = pd.DataFrame(df)

    def add_column_numeric(self,column_name,value):
        self.numeric[column_name]=value

    def add_column_open_df(self,column_name,value):
        self.open_df[column_name]=value

    def add_all_columns(self):
        self.numeric["Tip"]=self.tip
        self.numeric["Clasa"]=self.clasa
        self.numeric["Scoala"]=self.scoala
        self.open_df["Tip"] = self.tip
        self.open_df["Clasa"] = self.clasa
        self.open_df["Scoala"] = self.scoala








