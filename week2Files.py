# Week 2 - Files
# This script provides two simple examples of writing and reading files

# This block will open a file that already exists and write 500
# random numbers

file_loc = "C:\\DSA_OU\\boomerNumbers.txt"

import random
f = open(file_loc, 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close()


# Now lets read the file but 1st
# go back and save some typing

f = open(file_loc, 'r')
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number

f.close()

print("The sum is", theSum)


