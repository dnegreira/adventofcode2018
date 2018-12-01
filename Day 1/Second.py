#!/usr/bin/python3

start=0
results = list()

while True:
    found=False
    finput = open('input', 'r')
    for line in finput.read().splitlines():
        value = int(line)
        start = eval('start + value')
        if results.count(start) > 0:
            print("FOUND!")
            print(start)
            found=True
            break
        else:
            results.append(start)
            continue
    print(len(results))
    if found == True:
        break
finput.close()