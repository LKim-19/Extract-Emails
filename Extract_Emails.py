count = 0

fname = "mbox-short.txt"

fh = open(fname)

# For loop to split the lines up into individual words
# in the file as a list
for line in fh:
    x=line.split()
    # If From is in the list then it will print out the email which is the next word in the list also
    # keeps count of how many emails there are
    if 'From' in x:
        print(x[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
