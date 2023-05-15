import pandas as pd
import numpy as np
import re
class Extractor:
    '''
    extract data and necessarily information from the path
    '''
    open_questions=pd.DataFrame()
    numeric_questions=pd.DataFrame()

    def __init__(self,file_path):
        self.file_path=file_path

    def read_csv(self):
        '''
        read csv files
        '''
        date = pd.read_csv(self.file_path)
        date = date.dropna()
        self.numeric_questions = date[pd.to_numeric(date["Raspuns"], errors='coerce').notna()]
        self.open_questions = date[pd.to_numeric(date["Raspuns"], errors='coerce').isna()]


    def get_classes(self):
        '''
        get the class name from file path
        '''
        pattern = r"\d[A-Z]"  # we want to extract the class from the name of the path, class have the digit-uppercase format
        # the name of the file is School[digit][Upper Case].csv
        clasa = re.search(pattern, self.file_path)
        if clasa is not None:
            return clasa.group()
        else:
            return None

    def get_tip(self):
        '''
        get the type from file path
        '''
        tipuri = ["Elevi", "Parinti", "Profesori", "parinti", "profesori","elevi"]
        for i in tipuri:
            if i in self.file_path:
                i=i.capitalize()
                return i
        return None


    def get_scoala(self):
        '''
        get the school name from file path
        :return:
        '''
        scoli = ["scoala A", "scoala B", "scoala C", "scoala D"]
        for i in scoli:
            if i in self.file_path:
                return i
        return None
