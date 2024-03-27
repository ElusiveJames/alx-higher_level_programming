#!/usr/bin/python3
import sys
sum = 0
count = 1
while count <= len(sys.argv[1:]):
    sum += int(sys.argv[count])
    count += 1
print(sum)
