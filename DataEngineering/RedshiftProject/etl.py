import psycopg2
from functools import reduce
from sql_queries import copy_logs, copy_songs, insert_artists, insert_songs, insert_time, insert_users, insert_songplays
import configparser
from creating_tables import execute_query


config = configparser.ConfigParser()
configFilePath = r'C:\Users\The user\Documents\course\IntegralyticCourse\DataEngineering\RedshiftProject\configuration.cfg'
config.read(configFilePath)
DB_name = config.get('RedshiftInfo', 'DATABASE')
user_name = config.get('RedshiftInfo', 'USER')
host_name = config.get('RedshiftInfo', 'HOST')
pass_name = config.get('RedshiftInfo', 'PASSWORD')
port_name = config.get('RedshiftInfo', 'PORT')




def main():
    """Function to extract data from S3, transform and load to Redshift.

    Args:
        None

    Returns:
        None
    """
    conn = psycopg2.connect(database = DB_name,
                        user = user_name,
                        host= host_name,
                        password = pass_name,
                        port = port_name)
    
    cur = conn.cursor()
    execute_query(copy_logs, conn, cur)
    execute_query(copy_songs, conn, cur)
    execute_query(insert_users, conn, cur)
    execute_query(insert_songs, conn, cur)
    execute_query(insert_artists, conn, cur)
    execute_query(insert_time, conn, cur)
    execute_query(insert_songplays, conn, cur)
    conn.close()


if __name__ == '__main__':
    main()