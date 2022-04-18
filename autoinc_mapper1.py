#!/usr/bin/env python

import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	incident_id, incident_type, vin_number, make, model, year, incident_date, description= line.split(",")
	results = [vin_number, incident_type, make, year]
	print('%s\t%s\t%s\t%s' %(vin_number,incident_type,make,year))
