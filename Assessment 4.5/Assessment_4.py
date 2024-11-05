import pyodbc

class BackEnd():
    def allRec():
        db_file = r'C:\Users\2024001678\Downloads\Assessment 4.accdb'

      # establish a connection to the database
        conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
        conn = pyodbc.connect(conn_str)

       # create a cursor object to interact with the database
        cursor = conn.cursor()

        sqlComm = 'SELECT * FROM Company_Data;' # Replace YourTableName with your table name
   
        try:
            # Execute a SELECT query
            cursor.execute(sqlComm)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Print column headers
            columns = [column[0] for column in cursor.description]
            print(f'{"Company Name":<30}{"Industry":<30}{"Year Revenue":<20}{"Revenue Growth":<20}{"Number of employees":<20}{"Headquarters":<20}{"Foundation":<20}')

            # Print each row
            for row in rows:
                
                CoFoundDate=row.Foundation.strftime("%d-%m-%Y")
                
                Company_Data = f'{row.Company_name:<30}{row.Industry:<30}{row.Year_revenue:<20}{row.Revenue_growth:<20}{row.Number_of_employees:<20}{row.Headquarters:<20}{CoFoundDate:<20}'
                print(Company_Data)

        except pyodbc.Error as e:
            print(f"Error accessing database: {e}")

        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()
        
    def posGrowth():
        db_file = r'C:\Users\2024001678\Downloads\Assessment 4.accdb'

        # Establish a connection to the database
        conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
        conn = pyodbc.connect(conn_str)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        sqlComm = 'SELECT * FROM Company_Data WHERE Growth > 0;'

        try:
            # Execute a SELECT query
            cursor.execute(sqlComm)  # Replace YourTableName with your table name

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Print column headers
            columns = [column[0] for column in cursor.description]
            print('\t'.join(columns))

            # Print each row
            for row in rows:
                print('\t'.join(str(item) for item in row))

        except pyodbc.Error as e:
            print(f"Error accessing database: {e}")

        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()
        


