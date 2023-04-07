import mysql.connector
import os

from tabulate import tabulate
from dotenv import load_dotenv
from mysql_parser.parse_pcap import *

load_dotenv()


def main():
    # For every pcap file in pcap_samples

    # Connect and initialize MySQL database
    cnx, cursor = init_database("localhost", os.getenv(
        "MYSQL_USER"), os.getenv("MYSQL_PASSWORD"))

    # Parse the pcap file
    convert_pcap_to_table("pcap_samples/part1.pcap", cnx, cursor)

    # Ground truth answers
    for i in range(1, 8):
        sql_query = open(f"mysql_queries/q{i}.sql",
                         mode='r', encoding='utf-8-sig').read()
        result = query_table(sql_query, cnx)
        print(tabulate(result, headers='keys', tablefmt='psql'))

    ###############################
    ### Exp 1: Bare performance ###
    ###############################


    #################################
    ### Exp 2: Engligh variations ###
    #################################


    ##################################
    ### Exp 3: Language variations ###
    ##################################


    #####################################
    ### Exp 4: Adversarial variations ###
    #####################################



if __name__ == "__main__":
    main()
