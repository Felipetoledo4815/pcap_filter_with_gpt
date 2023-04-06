import mysql.connector
import pyshark

# Connect to MySQL server
cnx = mysql.connector.connect(host='localhost', user='root', password='password')
cursor = cnx.cursor()

# Create new database if it doesn't already exist
cursor.execute("CREATE DATABASE IF NOT EXISTS pcap_data")
cnx.database = 'pcap_data'

# Create packets table if it doesn't already exist
cursor.execute("DROP TABLE IF EXISTS packets")
cursor.execute("CREATE TABLE packets (id INT AUTO_INCREMENT PRIMARY KEY, src_ip VARCHAR(15), dst_ip VARCHAR(15), src_port INT, dst_port INT, protocol VARCHAR(10), length INT, timestamp DOUBLE, syn_flag INT, ack_flag INT, fin_flag INT, handshake VARCHAR(200), record VARCHAR(200))")

# Parse pcap file using PyShark
cap = pyshark.FileCapture('part1.pcap')

# Iterate through packets and insert into database
for pkt in cap:
    # Extract relevant fields
    timestamp = float(pkt.sniff_time.timestamp())
    src_ip = str(pkt.ip.src)
    dst_ip = str(pkt.ip.dst)
    src_port = int(pkt[pkt.transport_layer].srcport)
    dst_port = int(pkt[pkt.transport_layer].dstport)
    length = int(pkt.length)
    protocol = str(pkt.transport_layer)

    syn_flag = -1
    ack_flag = -1
    fin_flag = -1
    handshake = "None"
    record = "None"

    if "TCP" in str(pkt.layers):
        syn_flag = int(pkt.tcp.flags_syn)
        ack_flag = int(pkt.tcp.flags_ack)
        fin_flag = int(pkt.tcp.flags_fin)
    if "TLS" in str(pkt.layers):
        if "handshake" in pkt.tls.field_names:
            #print(pkt.tls.field_names)
            handshake = str(pkt.tls.handshake)

        if "record" in pkt.tls.field_names:
            record = str(pkt.tls.record)

    # Insert packet into database
    query = "INSERT INTO packets (src_ip, dst_ip, src_port, dst_port, protocol, length, timestamp, syn_flag, ack_flag, fin_flag, handshake, record) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (src_ip, dst_ip, src_port, dst_port, protocol, length, timestamp, syn_flag, ack_flag, fin_flag, handshake, record)
    cursor.execute(query, values)
    cnx.commit()

# Close database connection
cursor.close()
cnx.close()