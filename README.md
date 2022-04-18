# MapReduceHadoop

## Setup

1. Downloaded, Installed, and Booted Cloudera Virtual Machine instance via Oracle VirtualBox
2. Signed into Terminal as user: cloudera
3. From filemanager dashboard via http://localhost:8888/, directly uploaded data.csv to /input/
4. Made new directory /home/cloudera/AutoIncMapRed, and created:
-autoinc_mapper1.py
-autoinc_reducer1.py
-autoinc_mapper2.py
-autoinc_reducer2.py
-*1.py files form the basis of hdp_mapReduce1.sh
-*2.py files form the basis of hdp_mapReduce1.sh

## Test

-`[cloudera@quickstart AutoIncMapRed]$ hadoop fs -get /input/data.csv`
-`[cloudera@quickstart AutoIncMapRed]$ cat data.csv | ./autoinc_mapper1.py | sort | ./autoinc_reducer1.py | ./autoinc_mapper2.py | sort | ./autoinc_reducer2.py`
-`Toyota	2017	1`
-`Mercedes	2016	1`
-`Mercedes	2015	2`
-`Nissan	2003	1`

With the python code vetted, we execute the hadoop MapReduce jobs in two steps:

## MapReduce Step 1
Running:
  `./hdp_mapReduce1.sh`
Yields:
  `hdp_exec_log1.txt`
Results Found in:
  `hdp_results1.txt`

## MapReduce Step 2
Running:
  `./hdp_mapReduce2.sh`
Yields:
  `hdp_exec_log2.txt`
Results Found in:
  `hdp_results2.txt`

This file matches the output from our test, verifying our MapReduce ran correctly.
