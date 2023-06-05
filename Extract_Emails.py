count = 0

fname = "mbox-short.txt"

fh = open(fname)

for line in fh:
    x=line.split()
    if 'From' in x:
        print(x[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")