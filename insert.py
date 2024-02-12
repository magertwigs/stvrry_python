import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (21,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (22,'BOB KURIA',32,150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (23,'JANE MUTHONI',27,45000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (24,'MARY ANNE',38,280000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (25,'PAUL KAMAU',45,50000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()
