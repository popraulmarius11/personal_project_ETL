# Personal_project_ETL
### The project utilizes a separate file called "paths" to store the paths to the databases. Due to the confidential nature of the data, the actual data itself is not included in this project.
## Context
In the context of a project, I was entrusted with a significant number of databases collected from various schools. These databases contained survey responses from students, teachers, and parents. My task was to reorganize and transform the data using the program developed for this purpose. By applying data processing techniques, I aimed to make the data more suitable for in-depth analysis in Tableau Public.

After the data transformation process, I proceeded to create visualizations using Tableau Public. These visualizations effectively presented the key insights and trends discovered in the data. I shared the Tableau Public visualizations with my client, allowing them to gain valuable insights for decision-making purposes.

Overall, this project involved the extraction, transformation and analysis of data from multiple school databases. The combination of data processing techniques and Tableau Public facilitated the exploration and interpretation of the data, enabling informed decision-making based on the generated visualizations.

This project provides a data processing solution for working with databases that contain two columns: "Question" and "Answer". The "Answer" column can consist of values ranging from 1 to 5, representing a numeric rating, or it can contain open-ended responses.

## Project Description
This project is designed to extract, transform, and analyze data from multiple CSV databases. It provides a set of classes and functions for performing various data manipulation tasks such as aggregation, column dropping, adding new columns, sorting, and exporting the transformed data to Excel files.


## Documentation
### Classes
Extractor: Responsible for reading and extracting data from CSV databases.In order to retrieve additional information that was specific to each database, I had to extract relevant details from the folder path names. This step was necessary because certain details were not directly available within the databases themselves. By analyzing the path names, I was able to extract the required information and incorporate it into the data processing and visualization stages. This ensured that all pertinent data was considered and included in the final analysis and visualizations.

Transformer: Performs transformations on the extracted data, such as aggregating answers, adding columns, and preparing the data for further analysis.

DatabaseTransformer: Handles the overall transformation of the numeric and open-ended data(final databases) and provides methods for dropping columns, aggregating data, adding questions, and sorting.

Repository: Manages the collection of databases and provides methods for adding databases and accessing the final transformed data.

### Functions outside classes
read_database_paths(): Reads a text file containing paths to multiple CSV databases and returns a list of cleaned paths.
