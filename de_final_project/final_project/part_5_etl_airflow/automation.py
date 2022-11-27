import mysql.connector
import ibm_db

# Connect to MySQL
mysql_connection = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='sales'
)
mysql_cursor = mysql_connection.cursor()

# Connect to DB2
dsn_hostname = "2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
dsn_uid = "ytn38386"
dsn_pwd = ""
dsn_port = "30756"
dsn_database = "bludb"
dsn_driver = "jdbc:db2://2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:30756/bludb:user=ytn38386;password=uU6IYdF8Oa7T0400;sslConnection=true;"
dsn_protocol = "TCPIP"
dsn_security = "SSL"

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

# create db2 connection
db2_conn = ibm_db.connect(dsn, "", "")
print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

###############################################################################################################

# Find the last rowid from DB2 data warehouse
def get_last_rowid():
    SQL="SELECT MAX(rowid) FROM sales_data"
    stmt = ibm_db.exec_immediate(db2_conn, SQL)
    db_tuple = ibm_db.fetch_tuple(stmt)
    return db_tuple[0]

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
def get_latest_records(rowid):
    SQL = f"SELECT * FROM sales_data where rowid > {rowid}"
    mysql_cursor.execute(SQL)
    records = [row for row in mysql_cursor.fetchall()]
    return records

new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
def insert_records(records):
    SQL = "INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES(?,?,?,?);"
    for record in records:
        stmt = ibm_db.prepare(db2_conn, SQL)
        ibm_db.execute(stmt, record)

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
mysql_connection.close()
# disconnect from DB2 data warehouse
ibm_db.close(db2_conn)
