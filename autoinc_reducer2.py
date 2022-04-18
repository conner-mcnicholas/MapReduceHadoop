#!/usr/bin/env python
import sys

# [Define group level master information]
accdict = {}

# input comes from STDIN
for line in sys.stdin:
    # trimming spaces
    line = line.strip()

    # [parse the input from mapper]
    line= line.split('\t')
    make=line[0]
    year=line[1]
    count=line[2]

    # must convert string to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        accdict[(make,year)] = accdict[(make,year)]+count
    except:
        accdict[(make,year)] = count

# write tuples to STDOUT
for make,year in accdict.keys():
    print('%s\t%s\t%s' %(make,year, accdict[(make,year)]))
