#!/bin/bash

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar -file /home/cloudera/AutoIncMapRed/autoinc_mapper1.py -mapper "/home/cloudera/AutoIncMapRed/autoinc_mapper1.py" -file /home/cloudera/AutoIncMapRed/autoinc_reducer1.py -reducer "/home/cloudera/AutoIncMapRed/autoinc_reducer1.py" -input /input/data.csv -output /output/all_accidents
