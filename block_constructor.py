import csv
from collections import defaultdict

class Transaction:
    def __init__(self, txid, fee, weight):
        # Initializing transaction attributes
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = [] # storing parent transaction IDs in a list

def read_mempool_csv(file_path):
    # Reading the mempool CSV file and parse its contents
    mempool = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Parsing each row of the CSV file
            txid, fee, weight, parents = row[0].split(',')
            tx = Transaction(txid, fee, weight) # Creating Transaction object
            if parents:
                tx.parents = parents.split(';')  # Assigning parent transaction IDs
            mempool[txid] = tx     # Add Transaction object to mempool dictionary
    return mempool

def select_transactions(mempool, max_weight):
    # Select transactions for to be included in a block
    sorted_txs = sorted(mempool.values(), key=lambda x: x.fee, reverse=True)
    selected_txs = []  # List to store selected transaction IDs
    current_weight = 0  # Variable to track current total weight
    for tx in sorted_txs:
        # Checking weight constraints and parent transactions
        if tx.weight + current_weight <= max_weight:
            if all(parent in selected_txs for parent in tx.parents):
                selected_txs.append(tx.txid)  # Adding transaction ID to selected list
                current_weight += tx.weight  # Updating total weight
    return selected_txs

def main():
    mempool = read_mempool_csv('mempool.csv') # Read mempool CSV file
    max_weight = 4000000   # setting a Maximum block weight
    selected_txs = select_transactions(mempool, max_weight)  # Select transactions
    for txid in selected_txs:
        print(txid) # Print selected transaction IDs

if __name__ == "__main__":
    main() # Call main function if script is run directly
