import pyodbc

from datetime import date as dt


class Sql:
    def __init__(self, database_name, server_name="(LocalDB)\MSSQLLocalDB"):
        driver = '{SQL Server Native Client 11.0}'
        self.conn = pyodbc.connect(
            Trusted_Connection="yes",
            Driver=driver,
            Server=server_name,
            Database=database_name
        )
        self.query = "--{}\n\n-- Made in Python".format(dt.today().strftime("%d-%m-%Y"))

    def manual(self, query, response=False):
        cursor = self.conn.cursor()
        if response:
            return cursor.execute(query).fetchall()
        else:
            return False

sql = Sql('python_base')
temp = sql.manual("SELECT Name FROM sample", response=True)
for i in temp:
    print(i.Date)