import argparse
import os
from pathlib import Path
from mysql_parser.parse_pcap import *
from gpt_api.api import get_mysql_query

parser = argparse.ArgumentParser(
    prog='Pcap filter with GPT',
    description='Query a pcap file using natural language')

parser.add_argument(
    "-pcap",
    "--pcap",
    type=Path,
    required=True,
    dest='pcap',
    help="Path to the pcap file."
)
parser.add_argument(
    "-q",
    "--query",
    type=str,
    required=True,
    dest='query',
    help="Query in natural language."
)


def main():
    args = parser.parse_args()
    # Connect and initialize MySQL database
    cnx, cursor = init_database("localhost", os.getenv(
        "MYSQL_USER"), os.getenv("MYSQL_PASSWORD"))

    # Parse the pcap file
    convert_pcap_to_table(args.pcap, cnx, cursor)

    # TODO: Pass text to GPT and get a mysql query
    mysql_query = get_mysql_query(args.query)

    # Send query to table and retrieve result
    query = """ SELECT * FROM packets """
    result = query_table(cursor, query)

    print(result)

    # Close connection
    cursor.close()
    cnx.close()


if __name__ == "__main__":
    main()
