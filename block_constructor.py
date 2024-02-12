import csv
from collections import defaultdict

class Transaction:
    def __init__(self, txid, fee, weight):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = []

def read_mempool_csv(file_path):
    mempool = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            txid, fee, weight, parents = row[0].split(',')
            tx = Transaction(txid, fee, weight)
            if parents:
                tx.parents = parents.split(';')
            mempool[txid] = tx
    return mempool

def select_transactions(mempool, max_weight):
    sorted_txs = sorted(mempool.values(), key=lambda x: x.fee, reverse=True)
    selected_txs = []
    current_weight = 0
    for tx in sorted_txs:
        if tx.weight + current_weight <= max_weight:
            if all(parent in selected_txs for parent in tx.parents):
                selected_txs.append(tx.txid)
                current_weight += tx.weight
    return selected_txs

def main():
    mempool = read_mempool_csv('mempool.csv')
    max_weight = 4000000
    selected_txs = select_transactions(mempool, max_weight)
    for txid in selected_txs:
        print(txid)

if __name__ == "__main__":
    main()
