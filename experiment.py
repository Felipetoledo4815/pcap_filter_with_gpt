# import mysql.connector
import os
import time
import pickle
import argparse

from tabulate import tabulate
from tqdm import tqdm
from dotenv import load_dotenv
from mysql_parser.parse_pcap import *
from gpt_api.api import get_mysql_query

load_dotenv()

parser = argparse.ArgumentParser(prog='Tool experiment.')
parser.add_argument('--exp1', action='store_true')
parser.add_argument('--exp2', action='store_true')
parser.add_argument('--exp3', action='store_true')
parser.add_argument('--exp4', action='store_true')


def main():
    args = parser.parse_args()

    exp1 = {}
    exp2 = {}
    exp3 = {}
    exp4 = {}

    # For every pcap file in pcap_samples
    for pcap_file in os.listdir("pcap_samples"):
        # Connect and initialize MySQL database
        cnx, cursor = init_database("localhost", os.getenv(
            "MYSQL_USER"), os.getenv("MYSQL_PASSWORD"))

        # Parse the pcap file
        convert_pcap_to_table(f"./pcap_samples/{pcap_file}", cnx, cursor)

        # Ground truth answers
        ground_truth = []
        for i in range(1, 7):
            sql_query = open(f"mysql_queries/q{i}.sql",
                             mode='r', encoding='utf-8-sig').read()
            df = query_table(sql_query, cnx)
            ground_truth.append(df)
            # print(tabulate(result, headers='keys', tablefmt='psql'))

        """ Exp 1: Bare performance """
        if args.exp1:
            print(f"Running experiment 1 on {pcap_file}...")

            # Read .txt and save it to a list
            with open('./NL_queries/english_query_base.txt', 'r') as f:
                english_query_base = f.read().splitlines()

            exp1[pcap_file] = []
            for i, query in tqdm(enumerate(english_query_base), total=len(english_query_base)):
                start = time.time()
                # Pass text to GPT and get a mysql query
                mysql_query = get_mysql_query(query)
                # Send query to MySQL and retrieve result
                df = query_table(mysql_query, cnx)
                end = time.time()

                # Compare two pd.DataFrames
                status = False
                # if ground_truth[i].equals(df):
                if ground_truth[i].isin(df.values.ravel()).any().all():
                    status = True

                result = {
                    "status": status,
                    "query": query,
                    "gt_output": ground_truth[i],
                    "approach_output": df,
                    "time": end - start
                }
                exp1[pcap_file].append(result)

            # Save exp1 to a .pkl file
            with open('./experiment/exp1.pkl', 'wb') as f:
                pickle.dump(exp1, f)

        """ Exp 2: Engligh variations """

        """ Exp 3: Language variations """

        """ Exp 4: Adversarial variations """

        # Close connection
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    main()
