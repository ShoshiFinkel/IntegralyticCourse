<h2><strong>Project Description and Purpose:<strong><h2>
<h5>This project is about creating a SQL analytics database for a music streaming service called Sparkify. The goal is to help the analytics team understand what, when and how users are playing songs on the company's music app.
The data for the project is stored in JSON files:
<ul><li>song_data contains information about songs, such as the song title, artist name, and duration.</li>
<li>log_data contains information about user activity, such as the time of the activity, the user's ID, and the song they were listening to.</li><ul>
The first step in the project is to create a database schema. The schema is a blueprint for the database, and it defines the tables and columns that will be used to store the data. The schema for this project is a star schema, which means that there is one main fact table (songplays) and four dimensional tables (songs, artists, users, and time).
The next step is to load the data from the JSON files into the database. This is done using a Python script called etl.py. The script reads the JSON files, parses the data, and inserts it into the appropriate tables in the database.<h5>

<h2><strong>Project Structure:<strong><h2>
<h5><ul><li>sql_queries.py contains all your SQL queries, and is imported into the files bellow.</li>
<li>creating_tables.py drops and creates tables. You run this file to reset your tables before each time you run your ETL scripts.</li>
<li>configuration.cfg keeps all the configurations for creating a Redshift Serverless instance.</li>
<li>etl.py reads and processes files from song_data and log_data and loads them into your tables.</li><ul><h5>

<h2><strong>How to Run:<strong><h2>
<h5><ul><li>Run creating_tables.py from terminal to set up the database and tables.</li>
<li>Run etl.py from terminal to process and load data into the database.</li><ul><h5>

















