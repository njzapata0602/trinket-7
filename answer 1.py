#Nick Zapata
#Exercise 1

fname = raw_input("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print i
