#!/bin/bash
docker cp /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection/. 4c0d173b1e74:/src/Flask_textcollection
docker exec -t 4c0d173b1e74 /bin/bash -c "hdfs dfs -put /src/Flask_textcollection/*.txt /user/history/Flask_textcollection"
docker exec -t 4c0d173b1e74 /bin/bash -c "rm -r /src/Flask_textcollection/*.txt"
rm /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection/*.txt
