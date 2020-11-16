#!/bin/bash
docker cp /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection/. d14632e1dd51:/src/Flask_textcollection
cmd='/bin/bash -c "hdfs dfs -put /src/Flask_textcollection/*.txt /user/history/Flask/Flask_textcollection"'
docker_exec="docker exec -t d14632e1dd51 $cmd"
eval $docker_exec
cmd1='/bin/bash -c "rm /src/Flask_textcollection/*.txt"'
docker_exec1="docker exec -t d14632e1dd51 $cmd1"
eval $docker_exec1
rm /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection/*.txt
