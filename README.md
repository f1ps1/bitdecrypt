# bitdecrypt
A Bitcoin wallet collider with several utilities written in Python


## Installation

```bash
sudo apt update
sudo apt install -y git python3 python3-pip
pip3 install bitcoin
git clone https://github.com/f1ps1/bitdecrypt
```


## Run it

```bash
python3 crack.py <no. of threads (default 10)>
```

The python script now starts to generate bitcoin private keys + their corresponding public keys (stored in the `keys` directory).
Every thread stores its keys in a seperate file, so we have to merge them into one:


## Merge generated files

```bash
python3 merge.py
```

Now we can run a search algorithm over a file of bitcoin public keys to see if we got a match.
I included a file with the 1000 richest bitcoin addresses so you can see if you got a hit:


## Search keys

```bash
python3 search.py <database file (previously generated)> <one bitcoin address>
python3 search.py <database file (previously generated)> <a file containing a list of bitcoin addresses>
```

Simply, run:

```bash
python3 search.py keys/keys.total.db files/1000.richest
```

Good luck finding a private key!
