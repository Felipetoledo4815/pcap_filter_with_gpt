from tqdm import tqdm
from pathlib import Path
import mysql.connector
import pyshark
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=UserWarning)


def init_database(host_name, username, pw):
    # Connection to mysql server (enter your mysql info in these fields)
    cnx = mysql.connector.connect(host=host_name, user=username, password=pw)
    cursor = cnx.cursor()

    # Create new database if it doesn't already exist, named 'pcap_data'
    cursor.execute("CREATE DATABASE IF NOT EXISTS pcap_data")
    cnx.database = 'pcap_data'

    # Create a table in the database named 'packets' (overwrites!)
    cursor.execute("DROP TABLE IF EXISTS packets")
    cursor.execute("CREATE TABLE packets (id INT AUTO_INCREMENT PRIMARY KEY, src_ip VARCHAR(40), dst_ip VARCHAR(40), src_port INT, dst_port INT, protocol VARCHAR(10), length INT, timestamp DOUBLE, syn_flag INT, ack_flag INT, fin_flag INT, handshake VARCHAR(200), record VARCHAR(200))")
    return cnx, cursor


def convert_pcap_to_table(file, cnx, cursor):
    # Iterate through pcap file and insert into table
    print(f"Creating MySQL table from {Path(file).name}...")
    cap = pyshark.FileCapture(file)
    cap.load_packets()
    # For each packet...
    for pkt in tqdm(cap, total=len(cap)):
        timestamp = float(pkt.sniff_time.timestamp())
        src_ip = dst_pi = ""
        src_port = dst_port = -1

        if hasattr(pkt, 'ip'):
            src_ip = str(pkt.ip.src)
            dst_ip = str(pkt.ip.dst)
        elif hasattr(pkt, 'ipv6'):
            src_ip = str(pkt.ipv6.src)
            src_ip = str(pkt.ipv6.dst)

        if pkt.transport_layer:
            src_port = int(pkt[pkt.transport_layer].srcport)
            dst_port = int(pkt[pkt.transport_layer].dstport)

        length = int(pkt.length)
        protocol = str(pkt.transport_layer)

        syn_flag = ack_flag = fin_flag = -1
        handshake = record = ""

        if "TCP" in str(pkt.layers):
            syn_flag = int(pkt.tcp.flags_syn)
            ack_flag = int(pkt.tcp.flags_ack)
            fin_flag = int(pkt.tcp.flags_fin)

        if "TLS" in str(pkt.layers):
            if "handshake" in pkt.tls.field_names:
                # print(pkt.tls.field_names)
                handshake = str(pkt.tls.handshake)

            if "record" in pkt.tls.field_names:
                record = str(pkt.tls.record)

        # Insert info into database
        query = "INSERT INTO packets (src_ip, dst_ip, src_port, dst_port, protocol, length, timestamp, syn_flag, ack_flag, fin_flag, handshake, record) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (src_ip, dst_ip, src_port, dst_port, protocol, length,
                  timestamp, syn_flag, ack_flag, fin_flag, handshake, record)
        cursor.execute(query, values)
        cnx.commit()


def query_table(query, cnx):
    data = pd.read_sql(query, cnx)
    return data
