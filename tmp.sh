#!/bin/bash

docker run --rm -it --network=host -e DB_PORT=3308 -v /root/study/water-server/water/fixtures/mydata.json.xz:/app/water/fixtures/mydata.json.xz:ro water-server bash