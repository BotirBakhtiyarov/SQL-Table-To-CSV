# `sql_to_csv.py` Documentation

This Python script connects to a PostgreSQL database, retrieves data from a specified table, and saves it into a CSV file.

## Prerequisites

- **Python 3.x**
- **psycopg2 library**: Install using `pip install psycopg2`

## How to Use

1. Run the script:
   ```sh
   python sql_to_csv.py
   ```

2. Enter the required details when prompted:
   - **Database name**
   - **User name**
   - **Database host**
   - **Database password**
   - **Database port**
   - **Table name**

## Script Workflow

1. **Prompt for User Input**: The script asks for database connection details and the name of the table to export.
2. **Database Connection**: Establishes a connection to the PostgreSQL database using `psycopg2`.
3. **Create CSV File**: Creates an empty `data.csv` file in the current working directory.
4. **Data Export**: Uses the `COPY` SQL command to export the specified table's data into the `data.csv` file.
5. **Close Connection**: Closes the database connection and ends the script.

## Detailed Steps

1. **Prompts for Database Details**:
   ```python
   database_name = input("Enter Your Database name: ")
   User_name = input("Enter Your User name: ")
   host_local = input("Enter Your Database host: ")
   passord_code = input("Enter Your Database password: ")
   host_port = input("Enter Your Database port: ")
   table_name = input("Enter Your Database table name which you want to get: ")
   ```

2. **Establishes Connection**:
   ```python
   conn = psycopg2.connect(database=database_name, user=User_name, password=passord_code, host=host_local, port=host_port)
   conn.autocommit = True
   ```

3. **Creates an Empty CSV File**:
   ```python
   with open('data.csv', 'w') as my_data:
       pass
   print("Created data.csv File")
   ```

4. **Executes the `COPY` Command**:
   ```python
   cwd = os.getcwd()
   sql = """COPY {0} TO '{1}\\data.csv' DELIMITER ',' CSV HEADER""".format(table_name, cwd)
   cursor.execute(sql)
   print("Copying All data to data.csv file, please wait 10 sec...")
   time.sleep(10)
   ```

5. **Closes the Connection**:
   ```python
   conn.close()
   print("All Done")
   time.sleep(25)
   print("bye")
   ```

## Important Notes

- Ensure the PostgreSQL server is running and accessible.
- The user must have necessary permissions to read the table and perform the `COPY` operation.
- The script waits for 10 seconds after starting the copy operation to ensure it completes before closing the connection.

## Troubleshooting

- **Connection Issues**: Verify the database details (host, port, user, password) are correct.
- **Permission Errors**: Ensure the user has `SELECT` and `COPY` privileges on the specified table.
- **File Path Issues**: The script uses the current working directory. Make sure the script has write permissions in this directory.

## Example Usage

1. Run the script:
   ```sh
   python sql_to_csv.py
   ```
2. Enter the details when prompted:
   ```
   Enter Your Database name: mydatabase
   Enter Your User name: myuser
   Enter Your Database host: localhost
   Enter Your Database password: mypassword
   Enter Your Database port: 5432
   Enter Your Database table name which you want to get: mytable
   ```

This will create `data.csv` in the current directory containing the data from `mytable`.

