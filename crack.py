from bitcoin import *
import multiprocessing, sys, time

if sys.version_info[0] < 3:
	print("Python3 is required!")
	exit()

THREADS = 12
if (len(sys.argv) > 1):
	THREADS = int(sys.argv[1])
FILES = list(range(0, THREADS))

def crackTest():
	p = "test"
	start = time.time()
	for i in range(100):
		private_key = random_key()
		address = pubtoaddr(privtopub(private_key))
		with open("keys/keys." + str(p) + ".db", "a") as myfile:
			myfile.write(address + "-" + private_key + "\n")
	end = time.time()
	return 100 / (end - start)

def crack(p):
	print("Process " + str(p) + " starting...")
	try:
		while True:
			private_key = random_key()
			address = pubtoaddr(privtopub(private_key))
			with open("keys/keys." + str(p) + ".db", "a") as myfile:
				myfile.write(address + "-" + private_key + "\n")
	except KeyboardInterrupt:
		print("Process " + str(p) + " exiting...")

sys.stdout.write("Testing Algorithm... ")
sys.stdout.flush()
print("{:.2f} keys/second/thread".format(crackTest()))

for i in FILES:
	p = multiprocessing.Process(target=crack, args=(i,))
	p.start()
