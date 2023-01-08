'''ODBC module connect python to sql server'''
import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=LAPTOP-GT0CQGP6;"
                      "Database=Students;Trusted_Connection=yes;")

cursor = cnxn.cursor()

UPDATE_QUERY = "update Students set Email = 'masterarpit@gmail.com' where Name = 'Arpit'"
cursor.execute(UPDATE_QUERY)

cursor.execute('SELECT * FROM Students')

onerow = cursor.fetchone()
print(f"row = {onerow}")

allrow = cursor.fetchall()
for row in allrow:
    print(row)

amount = input("Enter Salary for Arpit")
UPDATE_QUERY = "update Students set Salary = "+amount.strip()+" where Name = 'Arpit'"
cursor.execute(UPDATE_QUERY)

cursor.commit()
cnxn.close()
