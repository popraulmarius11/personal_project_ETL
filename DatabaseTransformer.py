import pandas as pd
import numpy as np

class DatabaseTransformer:
    def __init__(self, numeric, open_df):
        self.numeric = numeric
        self.open_df = open_df


    def drop_column(self, column_name):
        '''
        drop a selected column
        '''
        self.numeric = self.numeric.drop(column_name, axis=1)

    def aggregate(self, column_names, aggregated_values):
        '''
        aggregate by sum selected values and columns
        '''
        self.numeric = self.numeric.groupby(column_names)[aggregated_values].sum().reset_index()

    def add_question(self):
        '''
        Add the question number before each question in the database
        '''
        tip_gr = self.numeric.groupby('Tip')
        for tip, f in tip_gr:
            el = f["Intrebari"].unique()
            for i in range(len(el)):
                self.numeric = self.numeric.replace(el[i], "Întrebarea " + str(i + 1) + ": " + el[i])

    def sort_questions(self, list_columns, order=[True]):
        '''
        sort by a specific column and order
        '''
        self.numeric = self.numeric.sort_values(list_columns, ascending=order)
