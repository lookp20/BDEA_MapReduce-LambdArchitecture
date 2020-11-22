#!/bin/bash

# input -> Alle Dokumente

docker exec -t 4c0d173b1e74 hdfs dfs -rm -r /user/history/output
docker exec -t 4c0d173b1e74 rm -r /src/output
rm -r /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output
docker exec -t 4c0d173b1e74 hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapred.reduce.tasks=4 -file /src/mapper2.py -mapper "python mapper2.py" -file /src/reducer.py  -reducer "python reducer.py" -input /user/history/Flask_textcollection/*.txt  -output /user/history/output -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf stream.map.output.field.separator=^ -jobconf stream.num.map.output.key.fields=4 -jobconf map.output.key.field.separator=^ -jobconf num.key.fields.for.partition=1
docker exec -t 4c0d173b1e74 hdfs dfs -get /user/history/output /src
docker cp 4c0d173b1e74:/src/output /Users/lookphanthavong/Documents/VisualStudioCode/BDEA
for file in /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output/output/part*; do mv "$file" "${file%.exec}.txt"; done


