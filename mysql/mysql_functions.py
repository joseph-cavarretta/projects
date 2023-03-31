import configparser
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

CONFIG_PATH = ''
config_parser = configparser.ConfigParser()
config_parser.read(CONFIG_PATH)


def mysql_connect():
    return mysql.connector.connect(
        user=config_parser.get('MYSQL', 'username'),
        password=config_parser.get('MYSQL', 'password'),
        host=config_parser.get('MYSQL', 'hostname'),
        database=config_parser.get('MYSQL', 'db')
    )


def mysql_get_creds():
    return dict(
        user=config_parser.get('MYSQL', 'username'),
        password=config_parser.get('MYSQL', 'password'),
        host=config_parser.get('MYSQL', 'hostname'),
        database=config_parser.get('MYSQL', 'db'),
        port=config_parser.get('MYSQL', 'port')
    )


def mysql_query(query):
    conn = mysql_connect()
    df = pd.read_sql(query, con=conn)
    conn.close()
    assert conn.is_connected() == False
    return df


def mysql_cursor_query(query):
    conn = mysql_connect()
    cursor = conn.cursor()
    cursor.execute(query)
    records = [row for row in cursor.fetchall()]
    conn.close()
    assert conn.is_connected() == False
    return records


def mysql_insert_row(query, data):
    conn = mysql_connect()
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    print(f'{cursor.rowcount} rows inserted')
    conn.close()
    assert conn.is_connected() == False


def mysql_insert_multiple(query, data):
    conn = mysql_connect()
    cursor = conn.cursor()
    cursor.executemany(query, data)
    conn.commit()
    print(f'{cursor.rowcount} rows inserted')
    conn.close()
    assert conn.is_connected() == False


def mysql_insert_dataframe(dataframe, table):
    creds = mysql_get_creds()
    eng = create_engine(
        f'mysql+mysqlconnector://{creds["user"]}:{creds["password"]}@{creds["host"]}:{creds["port"]}/{creds["db"]}', 
        echo=False)
    dataframe.to_sql(name=table, con=eng, if_exists='append', index=False)
    print(f'{len(dataframe)} rows inserted')