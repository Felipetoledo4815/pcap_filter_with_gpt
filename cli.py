import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='Pcap filter with GPT',
                    description='Query a pcap file using natural language')

parser.add_argument(
    "-pcap", 
    "--pcap",
    type=Path,
    required=True,
    help="Path to the pcap file."
)
parser.add_argument(
    "-q", 
    "--query",
    type=str,
    required=True,
    help="Query in natural language."
)

def main():
    print("Should parse the pcap file")
    print("Should pass text to GPT and get a mysql query")
    print("Should infer the database with the mysql query")
    print("Show results")

if __name__ == "__main__":
    main()