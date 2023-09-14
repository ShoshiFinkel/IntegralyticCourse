import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import psutil

class Cleaning:

    def __init__(self, conn):
        """
        Initializes the Cleaning connection object.
        
        Args:
            conn: A database connection object.
        """
        self.conn = conn
        self.cursor = self.conn.cursor()

    # Read the data to data frame.
    def read_data(self):
        """
        Reads data from the database table 'HouseFeatures' into a DataFrame.

        Returns:
            df: A pandas DataFrame containing the data.
        """
        df = pd.read_sql_query("SELECT * FROM HouseFeatures", self.conn)
        return df


    # We will create dummies columns.
    def make_categories(self,df):
        """
        Encodes categorical columns in the DataFrame as numeric using one-hot encoding.

        Args:
            df: The DataFrame to encode.

        Returns:
            df: The DataFrame with categorical columns encoded.
        """
        col_list = ['bedrooms', 'bathrooms', 'stories',
        'mainroad', 'guestroom', 'basement', 'hotwaterheating',
        'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
        for col in col_list:
            category=pd.Categorical(df[col])
            df[col]=category.codes
        return df
    
    def drop_column(self,df):
        """
        Drops the 'house_id' column from the DataFrame.

        Args:
            df: The DataFrame to remove the column from.

        Returns:
            df: The DataFrame with the 'house_id' column removed.
        """
        df.drop('house_id', axis=1, inplace=True)
        return df

    def split_data(self,df):
        """
        Splits the data into training and testing sets.
        
        Args:
            df: The DataFrame containing the dataset.
        
        Returns:
            X_train, X_test, y_train, y_test: The training and testing data splits.
        """
        X = df.drop('price', axis = 1)
        y = df['price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.15, random_state=417)
        return X_train, X_test, y_train, y_test

    def scale_data(self, X_train, X_test):
        """
        Scales the data using Min-Max scaling.
        
        Args:
            X_train: The training feature data.
            X_test: The testing feature data.
        
        Returns:
            X_train_scaled, X_test_scaled: The scaled training and testing feature data.
        """
        mms = MinMaxScaler()
        X_train_scaled= mms.fit_transform(X_train)
        X_test_scaled= mms.fit_transform(X_test)
        return X_train_scaled, X_test_scaled
    
class TrackMemoryUsage:

    def track_before_model(self):
        """
        Tracks memory and CPU usage before running a model.

        Returns:
            cpu_percent_before: CPU usage percentage before running the model.
            virtual_memory_used_before: Virtual memory used before running the model.
            virtual_memory_free_before: Virtual memory free before running the model.
            virtual_memory_percent_before: Virtual memory percentage before running the model.
            available_memory_before: Available memory percentage before running the model.
        """
        cpu_percent_before = psutil.cpu_percent()
        virtual_memory_used_before = psutil.virtual_memory().used
        virtual_memory_free_before = psutil.virtual_memory().free
        virtual_memory_percent_before = psutil.virtual_memory().percent
        available_memory_before = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        return cpu_percent_before, virtual_memory_used_before, virtual_memory_free_before, virtual_memory_percent_before, available_memory_before
    
    def track_after_model(self):
        """
        Tracks memory and CPU usage after running a model.

        Returns:
            cpu_percent_after: CPU usage percentage after running the model.
            virtual_memory_percent_after: Virtual memory percentage after running the model.
            virtual_memory_used_after: Virtual memory used after running the model.
            virtual_memory_free_after: Virtual memory free after running the model.
            available_memory_after: Available memory percentage after running the model.
        """
        cpu_percent_after = psutil.cpu_percent()
        virtual_memory_percent_after = psutil.virtual_memory().percent
        virtual_memory_used_after = psutil.virtual_memory().used
        virtual_memory_free_after = psutil.virtual_memory().free
        available_memory_after = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        return cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after, cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after
    
    
    def calculate_model_usage(self, cpu_percent_before, virtual_memory_used_before, virtual_memory_free_before, virtual_memory_percent_before, available_memory_before, cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after):
        """
        Calculates the resource usage by the model.

        Args:
            cpu_percent_before: CPU usage percentage before running the model.
            virtual_memory_used_before: Virtual memory used before running the model.
            virtual_memory_free_before: Virtual memory free before running the model.
            virtual_memory_percent_before: Virtual memory percentage before running the model.
            available_memory_before: Available memory percentage before running the model.
            cpu_percent_after: CPU usage percentage after running the model.
            virtual_memory_percent_after: Virtual memory percentage after running the model.
            virtual_memory_used_after: Virtual memory used after running the model.
            virtual_memory_free_after: Virtual memory free after running the model.
            available_memory_after: Available memory percentage after running the model.
            virtual_memory_percent_after: Virtual memory percentage after running the model.
        """
        cpu_percent = cpu_percent_after - cpu_percent_before
        virtual_memory_used = virtual_memory_used_after - virtual_memory_used_before
        virtual_memory_free = virtual_memory_free_after - virtual_memory_free_before
        virtual_memory_percent = virtual_memory_percent_after - virtual_memory_percent_before
        available_memory = available_memory_after - available_memory_before

        print('cpu_percent:', cpu_percent, '\navailable_memory:', available_memory, '\nvirtual_memory_percent:', virtual_memory_percent, '\nvirtual_memory_used:', virtual_memory_used, '\nvirtual_memory_free:', virtual_memory_free)

                    


class Model:

    def create_model(self,X_train_scaled, y_train, X_test_scaled, y_test):
        """
        Fits a linear regression model to the training data and evaluates it on the testing data.
        
        Args:
            X_train_scaled: The scaled training feature data.
            y_train: The training target data.
            X_test_scaled: The scaled testing feature data.
            y_test: The testing target data.
        """
        lr = LinearRegression()
        lr.fit(X_train_scaled, y_train)
        predictions = lr.predict(X_test_scaled)
        r = lr.score(X_test_scaled, y_test)
        print("R-square score:",r)
        RMSE = mean_squared_error(y_test, predictions, squared = False)
        print("RMSE:",RMSE)
        MAE = mean_absolute_error(y_test, predictions)
        print("MAE:",MAE)
    