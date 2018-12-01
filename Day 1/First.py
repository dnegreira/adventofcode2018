#!/usr/bin/python3
finput = open('input', 'r')

lines = finput.read().splitlines()

start=0

for line in lines:
    value = int(line)
    start = eval('start + value') 

print(start)
finput.close()