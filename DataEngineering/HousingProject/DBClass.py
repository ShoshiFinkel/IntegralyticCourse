import csv

class DB:

    def __init__(self, conn):
        """
        Initializes the DB object.
        
        Args:
            conn: A database connection object.
        """
        self.conn = conn
        self.cursor = self.conn.cursor()

    # Create the HouseFeatures table.
    def create_table(self):
        """
        Creates the 'HouseFeatures' table in the database if it does not exist.

        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS HouseFeatures(
            house_id MEDIUMINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            price BIGINT,
            area INT,
            bedrooms SMALLINT,
            bathrooms SMALLINT,
            stories SMALLINT,
            mainroad NVARCHAR(3),
            guestroom NVARCHAR(3),
            basement NVARCHAR(3),
            hotwaterheating NVARCHAR(3),
            airconditioning NVARCHAR(3),
            parking SMALLINT,
            prefarea NVARCHAR(3),
            furnishingstatus NVARCHAR(20)
            )''')
        self.conn.commit()

    # Insert data into the DB from CSV file.
    def csv_to_db(self, file):
        """
        Inserts data from a CSV file into the 'HouseFeatures' table in the database.

        Args:
            file: The path to the CSV file containing the data to be inserted.

        """
        with open (file, 'r') as f:
            reader = csv.reader(f)
            columns = next(reader)
            query = 'insert into HouseFeatures({0}) values ({1})'
            query = query.format(','.join(columns), ','.join(['%s'] * len(columns)))
            cursor = self.conn.cursor()
            for data in reader:
                cursor.execute(query, data)
            self.conn.commit()
    
 