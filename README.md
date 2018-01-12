#Exercise 1

fname = raw_input("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print i


#Exercise 2

fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
count = 0
tot = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
ans = tot / count
print "Average spam confidence:", ans


#Exercise 3


python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs - this is just
an exercise.
'''
import sys

user_data = raw_input("Enter the file name: ")

if user_data == "na na boo boo":
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    sys.exit(0)

try:
    user_file = open(user_data, 'r')
except:
    print "File cannot be opened: " + user_data
    sys.exit(1)


lines_list = [line.strip("\n") for line in user_file]


def count_subject_lines(data):
    subject_count = 0
    for line in lines_list:
        if line.startswith("Subject"):
            subject_count += 1
    print subject_count

count_subject_lines(lines_list)
