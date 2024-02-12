# BLOCK SAMPLE

```markdown
2e3da8fbc1eaca8ed9b7c2db9e6545d8ccac3c67deadee95db050e41c1eedfc0
6eb38fad135e38a93cb47a15a5f953cbc0563fd84bf1abdec578c2af302e10bf
79c51c9d4124c5cbb37a85263748dcf44e182dff83561fa3087f0e9e43f41c33
8c25f9be93990b96e8bc363778d6debee6867c7d73cefab69405d41e677b536c
```

# BLOCK CONSTRUCTOR Challenge

This challenge offers an opportunity to demonstrate your problem-solving and coding skills in the context of Bitcoin mining.

# The Problem:

Bitcoin miners construct blocks by selecting transactions from their mempool. Each transaction includes:

- A fee collected by the miner if included in the block.
- A weight indicating its size.
- Optional parent transactions within the mempool.

The miner builds an ordered list of transactions with a combined weight below the maximum block weight (`4,000,000`). Transactions with parent transactions can only be included if their parents appear earlier in the list. The goal is to maximize the total fee for the miner.

# Your Task:

Write a program that reads a `mempool.csv` file in the following format:

```
<txid>,<fee>,<weight>,<parent_txids>
```

- `txid`: Transaction identifier.
- `fee`: Transaction fee in satoshis.
- `weight`: Transaction weight in bytes.
- `parent_txids`: Semicolon-separated list of parent transaction IDs (optional).

The program should output valid block contents, consisting of transaction IDs separated by newlines, while adhering to these constraints:

- Transactions must appear in order.
- No transaction appears unless its parents are included.
- No transaction appears before its parents.
- No transaction appears more than once.

# Mempool Sample:

```
2e3da8fbc1eaca8ed9b7c2db9e6545d8ccac3c67deadee95db050e41c1eedfc0,452,1620,
9d317fb308fd5451fd0ec612165638cb9e37bd8aa8918dff99a48fe05224276f,350,1400,288ea91bb52d8cb28289f4db0d857356622e39e78f33f26bf6df2bbdd3810fad;b5b993bda3c23bdefe4a1cf75b1f7cbdfe43058f2e4e7e25898f449375bb685c;c1ae3a82e52066b670e43116e7bfbcb6fa0abe16088f920060fa41e09715db7d
```

# Key Considerations:

- The total weight of transactions in a block must not exceed the maximum limit.
- There's no coinbase transaction in this exercise.
- Transactions with missing or invalid parent references are excluded.
- Transactions appear in the output only if their parents are included and in the correct order.
- No transaction appears more than once.

**General Advice:**

1. Start with a simple solution that builds a valid block, then refine it for optimization.
2. Explain your reasoning, design choices, and trade-offs clearly.
3. Implement the solution yourself, attributing any external code.

