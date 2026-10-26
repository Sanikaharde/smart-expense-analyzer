import pymssql

conn = pymssql.connect(
    server='LAPTOP-707J6I72',
    database='smart_expense_db',
    trusted=True
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

for row in cursor:
    print(row)

conn.close()