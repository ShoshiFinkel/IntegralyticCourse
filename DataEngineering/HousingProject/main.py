import pandas as pd
import pymysql
from DBClass import DB
from CreateModel import Cleaning, Model, TrackMemoryUsage
import logging
import LoggingFile as lf
import traceback


def main():
    """
    The main function that orchestrates the data processing and modeling workflow.

    This function connects to a MySQL database, creates a table if it does not exist,
    loads data from a CSV file into the table, performs data cleaning and preprocessing,
    trains a machine learning model, and tracks memory and CPU usage before and after
    running the model.

    """
    logging.basicConfig(filename =  lf.LOG_FILE,
                    filemode = 'a+',
                    format = '%(asctime)s ,%(msecs)d %(name)s  %(levelname)s  %(message)s',
                    datefmt = '%H:%M:%S',
                    level = logging.INFO)

    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='Sf@323895474', db='sys')
        logging.info("A connection to the database was created successfully")
    except ValueError as exc:
        logging.error(traceback.format_exc())

    db = DB(conn)
    try:
        db.create_table()
        logging.info("A table was created successfully")
    except ValueError as exc:
        logging.error(traceback.format_exc())
    try:
        db.csv_to_db('C:/Users/The user/Documents/course/IntegralyticCourse/DataEngineering/HousingProject/Housing.csv')
        logging.info("CSV file was loaded to the new table.")
    except ValueError as exc:
        logging.error(traceback.format_exc())   
    cleaning = Cleaning(conn)
    df = cleaning.read_data()
    df = cleaning.make_categories(df)
    df = cleaning.drop_column(df)
    X_train, X_test, y_train, y_test = cleaning.split_data(df)
    X_train_scaled, X_test_scaled = cleaning.scale_data(X_train, X_test)
    model = Model()
    track = TrackMemoryUsage()
    cpu_percent_before, virtual_memory_used_before, virtual_memory_free_before, virtual_memory_percent_before, available_memory_before = track.track_before_model()
    model.create_model(X_train_scaled, y_train, X_test_scaled, y_test)
    cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after, cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after = track.track_after_model()
    track.calculate_model_usage(cpu_percent_before, virtual_memory_used_before, virtual_memory_free_before, virtual_memory_percent_before, available_memory_before, cpu_percent_after, virtual_memory_used_after, virtual_memory_free_after, available_memory_after, virtual_memory_percent_after)
    conn.close()




if __name__ == '__main__':
    main()