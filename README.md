# MapReduceHadoop

## Setup

1. Installed Oracle VirtualBox
2. Installed Cloudera VM instance, Imported to VirtualBox, Started VM
3. Signed into Terminal as user: cloudera
4. The python scripts in this repository are compatible with python2, which the machine has pre-installed.
5. From filemanager dashboard via http://localhost:8888/, directly uploaded data.csv to /input/
6. Made new directory /home/cloudera/AutoIncMapRed, and created:
```
autoinc_mapper1.py
autoinc_reducer1.py
autoinc_mapper2.py
autoinc_reducer2.py
```
*1.py files form the basis of hdp_mapReduce1.sh\
*2.py files form the basis of hdp_mapReduce2.sh

## Test

```
[cloudera@quickstart AutoIncMapRed]$ #must remember to allow execute permissions on python scripts
[cloudera@quickstart AutoIncMapRed]$ chmod +x *.py
[cloudera@quickstart AutoIncMapRed]$ hadoop fs -get /input/data.csv```
[cloudera@quickstart AutoIncMapRed]$ cat data.csv | ./autoinc_mapper1.py | sort | ./autoinc_reducer1.py | ./autoinc_mapper2.py | sort | ./autoinc_reducer2.py
Toyota	2017	1
Mercedes	2016	1
Mercedes	2015	2
Nissan	2003	1
```

With the python code vetted, we execute the hadoop MapReduce jobs in two steps.  

```
[cloudera@quickstart AutoIncMapRed]$ #must remember to allow execute permissions on shell scripts
[cloudera@quickstart AutoIncMapRed]$ chmod +x *.sh
```

## MapReduce Step 1
Running:\
  `./hdp_mapReduce1.sh`\
Yields:\
  `hdp_exec_log1.txt`\
Results Found in:\
  `hdp_results1.txt`\

## MapReduce Step 2
Running:\
  `./hdp_mapReduce2.sh`\
Yields:\
  `hdp_exec_log2.txt`\
Results Found in:\
  `hdp_results2.txt`\

The 4 python scripts are the only details not available in this summary:
```
[cloudera@quickstart AutoIncMapRed]$ #mapReduce1
[cloudera@quickstart AutoIncMapRed]$ hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/AutoIncMapRed/autoinc_mapper1.py -mapper "/home/cloudera/AutoIncMapRed/autoinc_mapper1.py" \
-file /home/cloudera/AutoIncMapRed/autoinc_reducer1.py -reducer "/home/cloudera/AutoIncMapRed/autoinc_reducer1.py" \
-input /input/data.csv -output /output/all_accidents

[cloudera@quickstart AutoIncMapRed]$ #mapReduce2
[cloudera@quickstart AutoIncMapRed]$ hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/AutoIncMapRed/autoinc_mapper2.py -mapper "/home/cloudera/AutoIncMapRed/autoinc_mapper2.py" \
-file /home/cloudera/AutoIncMapRed/autoinc_reducer2.py -reducer "/home/cloudera/AutoIncMapRed/autoinc_reducer2.py" \
-input /output/all_accidents -output /output/make_year_count

[cloudera@quickstart AutoIncMapRed]$ #retrieving output file directory of mapReduce2 from HDFS to VM drive
[cloudera@quickstart AutoIncMapRed]$ hadoop fs -get /output/make_year_count

[cloudera@quickstart AutoIncMapRed]$ #viewing results of output file from mapReduce2
[cloudera@quickstart AutoIncMapRed]$ cat make_year_count/*
Toyota	2017	1
Mercedes	2016	1
Mercedes	2015	2
Nissan	2003	1
```
This output matches our test, verifying the MapReduce ran as intended.
