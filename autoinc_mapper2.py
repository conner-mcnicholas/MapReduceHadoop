#!/usr/bin/env python
import sys

# input comes from STDIN
for line in sys.stdin:
# [derive mapper output key values]
	line = line.strip()
	line = line.split('\t')
	make=line[1]
	year=line[2]
	print('%s\t%s\t%d' %(make,year,1))
