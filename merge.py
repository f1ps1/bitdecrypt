import os, sys

if sys.version_info[0] < 3:
	print("Python3 is required!")
	exit()

database = "keys/keys.total.db"
folder = "keys/"

file_list = os.listdir(folder)
target = open(database, "a");
for filename in sorted(file_list):
	if (folder + filename == database):
		continue # ignore the collective file
	print("Merging " + folder + filename + "  ", end="\r")
	with open(folder + filename) as infile:
		for line in infile:
			target.write(line);
	os.remove(folder + filename)

print("Merged all files!" + (" " * 10))

def sizefmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

print("")
print(" Outfile: " + database)
print("    Size: {:,}".format(os.path.getsize(database)))
print("  Size f: " + sizefmt(os.path.getsize(database)))
print(" Entries: {:,}".format(sum(1 for line in open(database))))
