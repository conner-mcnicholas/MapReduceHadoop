#!/usr/bin/env python

import sys
# [Define group level master information]

current_vin =  None
vin = None
make = None
year = None

def reset():
# [Logic to reset master info for every new group]
	current_vin =  None
	vin = None
	make = None
	year = None

# Run for end of every group
def flush():
	# [Write the output]
	print('%s\t%s\t%s' %(current_vin,make,year))

# input comes from STDIN
for line in sys.stdin:

	line = line.strip()

	# [parse the input we got from mapper and update the master info]
	line= line.split("\t")
	vin = line[0]
	incident_type= line[1]

	if current_vin == vin:
		if incident_type == 'I':
			make= line[2]
			year= line[3]


	# [detect key changes]
	if current_vin != vin:
		if current_vin != None:
			# write result to STDOUT
			flush()
		reset()

	# [update more master info after the key change handling]
	if incident_type == 'I':
		make= line[2]
		year= line[3]
	current_vin = vin

# do not forget to output the last group if needed!
flush()
