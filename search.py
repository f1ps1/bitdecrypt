import os, sys, hashlib

if sys.version_info[0] < 3:
	print("Python3 is required!")
	exit()

def sha256(arg) :
	byte_array = bytearray.fromhex(arg)
	m = hashlib.sha256()
	m.update(byte_array)
	return m.hexdigest()

def b58encode(hex_string) :
	alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	num = int(hex_string, 16)
	encode = ""
	base_count = len(alphabet)
	while (num > 0) :
		num, res = divmod(num,base_count)
		encode = alphabet[res] + encode
	return encode

def wif(priv) :
	_priv = priv.lower()
	priv_add_x80 = "80" + _priv
	first_sha256 = sha256(priv_add_x80)
	seconf_sha256 = sha256(first_sha256)
	first_4_bytes = seconf_sha256[0:8]
	resulting_hex = priv_add_x80 + first_4_bytes
	result_wif = b58encode(resulting_hex)
	return result_wif

filename = ""
address = ""

try:
	filename = sys.argv[1]
	address = sys.argv[2]
except Exception:
	print("Usage: python search.py <database file> <bitcoin address>")
	print("       python search.py <database file> <file of bitcoin addresses>")
	exit();


def checkAddress(ad, address):
	return ad == address

def success(line):
	print("")
	print("Found private key!\n")
	print("     Address: " + line.split("-")[0])
	print(" Private Key: " + line.split("-")[1].replace("\n", ""))
	print("         WIF: " + wif(line.split("-")[1].replace("\n", "")))
	exit()

keys = 0
pointer = 0
addresses = []

with open(filename) as target:
	for line in target:
		keys += 1
	print("Searching through {:,} cracked keys".format(keys))

if (os.path.isfile(address)):
	print("Opening " + address + " and checking for matches")

	with open(address) as target:
		for line in target:
			addresses.append(line.replace("\n", ""))
		print("Found {:,} addresses".format(len(addresses)))
else:
	addresses.append(address)

with open(filename) as infile:
	for line in infile:
		pointer += 1
		print("Checked {:,} / {:,} ({:.2f} %) keys".format(pointer, keys, 100*pointer/keys), end="\r")
		if (line.split("-")[0] in addresses):
			success(line)

print("\nNo private key found!")
exit()
