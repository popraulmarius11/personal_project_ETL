from Extractor import Extractor
from Transformer import Transformer
from DatabaseTransformer import DatabaseTransformer
import unittest
from Tests import *
from Repository import Repository

def read_database_paths():
    """
    Reads a text file containing paths to multiple CSV databases and returns a list of cleaned paths.
    """
    with open('paths', 'r') as file: #the file does not contain the real paths because those databases were private
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        lines = [line.strip().strip('"') for line in lines]
    return lines

if __name__ == '__main__':
    #unittest.main()
    lines = read_database_paths()
    repository = Repository()  # Create an instance of the Repository class

    for file_path in lines:
        extractor = Extractor(file_path)
        extractor.read_csv()
        transformer = Transformer(extractor.numeric_questions, extractor.open_questions,
                                  extractor.get_classes(), extractor.get_tip(), extractor.get_scoala())
        transformer.aggregate_answers()
        transformer.add_all_columns()
        repository.add_database(transformer.numeric, transformer.open_df)
    numeric_database = repository.final_database_numeric
    open_database = repository.final_database_open
    databasetransformer=DatabaseTransformer(numeric_database,open_database)
    databasetransformer.drop_column("Clasa")
    databasetransformer.aggregate(["Tip", "Scoala", "Intrebari", "Raspuns"],["Numar"])
    databasetransformer.add_question()
    databasetransformer.sort_questions("Intrebari")
    print(databasetransformer.numeric)
    final=databasetransformer.numeric
    deschise=databasetransformer.open_df
    final.to_excel(r"")
    deschise.to_excel(r"")
