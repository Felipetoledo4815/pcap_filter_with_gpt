import mysql.connector
import pyshark

# Connection to mysql server (enter your mysql info in these fields)
cnx = mysql.connector.connect(host='localhost', user='root', password='password')
cursor = cnx.cursor()

# fetch and print rows from the table

cursor.execute(""" USE pcap_data """)
cursor.execute(""" SELECT * FROM packets """)

data = cursor.fetchall()
for row in data:
    print(row)