#!/bin/bash

docker run -d --network=host -e DB_PORT=3308 --name water-server water-server