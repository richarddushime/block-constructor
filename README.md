# Block Constructor

This Python script selects transactions from a mempool CSV file to construct a block, maximizing the total fee to the miner. Each transaction in the mempool includes a fee, weight, and optional parent transactions.

The full challenge is [Here](https://github.com/richarddushime/block-constructor/blob/main/Block-constructor-challenge.md)

To Run the script follow the below steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/richarddushime/block-constructor.git
   ```
   Then 
   ```
   cd block-constructor
   ```

2. **Dependencies:**
The only dependency you will need is the [`mempool.csv`](https://github.com/richarddushime/block-constructor/blob/main/mempool.csv) file.

3. **Run the Script:**
   Execute the following command in your terminal to run the script:
   ```
   python3 block_constructor.py
   ```

4. **Output:**
   The script will print the selected transaction IDs for the constructed block.
   check the `sample_output.txt`file
