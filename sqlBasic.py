import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    # database="batch_db_new"    '''used to access database, it is unifunctional'''
)

sql = connection.cursor()

# create database database_name;

def create_db(db_name):
    query = "create database if not exists "+db_name
    sql.execute(query)
    print("database created")

create_db("batch_db_new")

sql.execute("use batch_db_new")      # '''used to use database, it if multi=functional'''

"""create table table_name
        (column_name data_type(length))
        (column_name data_type(length))
        (column_name data_type(length))
"""

def table_create(tb_name):
    query = "create table if not exists "+ tb_name + "(id int primary key,name varchar(30),city varchar(30),mobile int)"
    sql.execute(query)
    print(query)



table_create("test_record")



print("let's insert the element")

query = "insert into test_record values(4,'yash','patiala',12345)"

print("query")

sql.execute(query)

connection.commit()