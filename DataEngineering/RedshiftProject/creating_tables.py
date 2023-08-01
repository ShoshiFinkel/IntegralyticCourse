import psycopg2
from sql_queries import create_log_data, create_song_data, create_dtable_users, create_dtable_artists, create_dtable_songs, create_dtable_time, create_ftable_songplays
import configparser
 # Read the configuration file, and assign the configuration's variables.
config = configparser.ConfigParser()
configFilePath = r'C:\Users\The user\Documents\course\IntegralyticCourse\DataEngineering\RedshiftProject\configuration.cfg'
config.read(configFilePath)
DB_name = config.get('RedshiftInfo', 'DATABASE')
user_name = config.get('RedshiftInfo', 'USER')
host_name = config.get('RedshiftInfo', 'HOST')
pass_name = config.get('RedshiftInfo', 'PASSWORD')
port_name = config.get('RedshiftInfo', 'PORT')


def execute_query(query, cur, conn):
    """Function to execute queries, commit them or rollback and print the error message.

    Args:
        query: The query to execute.
        conn: The connection string.
        cur: The cursor.

    Returns:
        None
    """
    try:
        cur.execute(query)
        conn.commit()
    except Exception as ex:
        print(ex)
        conn.rollback()

def main():
    """Function to create DB's tables: log_data, song_data, ftable_songplays, dtable_users, dtable_songs, dtable_artists, dtable_time.

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
    execute_query(create_log_data, cur, conn)
    execute_query(create_song_data, cur, conn)
    execute_query(create_ftable_songplays, cur, conn)
    execute_query(create_dtable_users, cur, conn)
    execute_query(create_dtable_songs, cur, conn)
    execute_query(create_dtable_artists, cur, conn)
    execute_query(create_dtable_time, cur, conn)
    conn.close()

if __name__ == '__main__':
    main()

