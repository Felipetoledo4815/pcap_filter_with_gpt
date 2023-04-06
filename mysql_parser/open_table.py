import mysql.connector
import pyshark

# Connect to MySQL server
cnx = mysql.connector.connect(host='localhost', user='root', password='password')
cursor = cnx.cursor()

if cnx.is_connected():
    print('Connected to MySQL database')
cursor.execute(""" USE pcap_data """)
cursor.execute(""" SELECT * FROM packets """)

# fetch and print rows from the table
data = cursor.fetchall ()
for row in data:
    print(row)