#!/bin/bash

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -file /home/cloudera/AutoIncMapRed/autoinc_mapper2.py -mapper "/home/cloudera/AutoIncMapRed/autoinc_mapper2.py" -file /home/cloudera/AutoIncMapRed/autoinc_reducer2.py -reducer "/home/cloudera/AutoIncMapRed/autoinc_reducer2.py" -input /output/all_accidents -output /output/make_year_count
