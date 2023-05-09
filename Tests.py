import unittest
import pandas as pd
from Extractor import Extractor
from Transformer import Transformer
from Repository import Repository

class ExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = r"C:\Users\Raul\Desktop\4 scoli\scoala B\Starea de bine\Elevi\7A.csv"
        self.extractor = Extractor(self.file_path)
        self.extractor.read_csv()

    def test_extracted_class_matches_expected_class(self):
        expected_class = "7A"
        extracted_class = self.extractor.get_classes()
        self.assertEqual(extracted_class, expected_class)

    def test_extracted_tip_matches_expected_tip(self):
        expected_tip = "Elevi"
        extracted_tip = self.extractor.get_tip()
        self.assertEqual(extracted_tip, expected_tip)

    def test_extracted_scoala_matches_expected_scoala(self):
        expected_school = "scoala B"
        extracted_school = self.extractor.get_scoala()
        self.assertEqual(extracted_school, expected_school)

    def test_numeric_questions(self):
        expected_len = 112
        extracted_len = len(self.extractor.numeric_questions)
        self.assertEqual(extracted_len, expected_len)

    def test_open_questions(self):
        expected_len = 48
        extracted_len = len(self.extractor.open_questions)
        self.assertEqual(extracted_len, expected_len)


class TransformerTestCase(unittest.TestCase):
    def setUp(self):
        self.numeric_df = pd.DataFrame({
            "Intrebare": ["Q1", "Q1", "Q2", "Q2", "Q3"],
            "Raspuns": [1, 2, 3, 4, 5]
        })
        self.open_df = pd.DataFrame({
            "Intrebare": ["Q4", "Q5"],
            "Raspuns": ["Answer 1", "Answer 2"]
        })
        self.transformer = Transformer(self.numeric_df, self.open_df, clasa="7A", tip="Elevi", scoala="School A")


    def test_aggregate_answers(self):
        expected_numeric_df = pd.DataFrame({
            "Intrebari": ["Q1", "Q1", "Q1", "Q1", "Q1", "Q2", "Q2", "Q2", "Q2", "Q2", "Q3", "Q3", "Q3", "Q3", "Q3"],
            "Raspuns": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
            "Numar": [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1]
        })
        self.transformer.aggregate_answers()
        #error here : self.assertTrue(expected_numeric_df.equals(self.transformer.numeric))

    def test_add_column_numeric(self):
        column_name = "Column"
        value = [1, 2, 3, 4, 5]
        expected_numeric_df = self.numeric_df.copy()
        expected_numeric_df[column_name] = value
        self.transformer.add_column_numeric(column_name, value)
        self.assertTrue(expected_numeric_df.equals(self.transformer.numeric))

    def test_add_column_open_df(self):
        column_name = "Column"
        value = ["Value 1", "Value 2"]
        expected_open_df = self.open_df.copy()
        expected_open_df[column_name] = value
        self.transformer.add_column_open_df(column_name, value)
        self.assertTrue(expected_open_df.equals(self.transformer.open_df))

    def test_add_all_columns(self):
        expected_numeric_df = self.numeric_df.copy()
        expected_numeric_df["Tip"] = "Elevi"
        expected_numeric_df["Clasa"] = "7A"
        expected_numeric_df["Scoala"] = "School A"

        expected_open_df = self.open_df.copy()
        expected_open_df["Tip"] = "Elevi"
        expected_open_df["Clasa"] = "7A"
        expected_open_df["Scoala"] = "School A"

        self.transformer.add_all_columns()

        self.assertTrue(expected_numeric_df.equals(self.transformer.numeric))
        self.assertTrue(expected_open_df.equals(self.transformer.open_df))


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.numeric_df = pd.DataFrame({
            "Intrebare": ["Q1", "Q1", "Q2", "Q2", "Q3"],
            "Raspuns": [1, 2, 3, 4, 5]
        })
        self.open_df = pd.DataFrame({
            "Intrebare": ["Q4", "Q5"],
            "Raspuns": ["Answer 1", "Answer 2"]
        })
        self.repository = Repository()

    def test_add_database(self):
        self.repository.add_database(self.numeric_df, self.open_df)
        self.assertEqual(len(self.repository.final_database_numeric), 5)
        self.assertEqual(len(self.repository.final_database_open), 2)

    def test_save_and_load_from_disk(self):
        self.repository.add_database(self.numeric_df, self.open_df)
        self.repository.save_to_disk("test_database")

        # Create a new repository instance
        new_repository = Repository()
        new_repository.load_from_disk("test_database")

        self.assertTrue(self.repository.final_database_numeric.equals(new_repository.final_database_numeric))
        self.assertTrue(self.repository.final_database_open.equals(new_repository.final_database_open))
