#!/bin/bash
docker cp /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/images/. 4c0d173b1e74:/src/Flask_imgcollection
docker exec -t 4c0d173b1e74 /bin/bash -c "hdfs dfs -put /src/Flask_imgcollection/*.png /user/history/Flask_imgcollection"
docker exec -t 4c0d173b1e74 /bin/bash -c "rm -r /src/Flask_imgcollection/*.png"
rm /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/images/*.png
