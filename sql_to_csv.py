import psycopg2
import os
import csv
import time


database_name = input("Enter Your Database name: ")
User_name = input("Enter Your User name: ")
host_local = input("Enter Your Database host: ")
passord_code = input("Enter Your Database password: ")
host_port = input("Enter Your Database port: ")
table_name = input("Enter Your Database table name which you want to get: ")

cwd = os.getcwd()
conn = psycopg2.connect(database =database_name,
						user=User_name,
						password=passord_code,
						host=host_local,
						port=host_port)

conn.autocommit = True

cursor = conn.cursor()
time.sleep(2)
with open('data.csv','w') as my_data:
	pass
print("Created data.csv File")
print("Copying All data to data.csv file, please wait 10 sec...")
time.sleep(10)

sql = """COPY {0} TO '{1}\\data.csv' DELIMITER ',' CSV HEADER""".format(table_name,cwd)

cursor.execute(sql)

conn.close()
print("All Done")
time.sleep(25)
print("bye")
