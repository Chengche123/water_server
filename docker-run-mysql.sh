#!/bin/bash

docker run --name mysql -d -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=KJ402 mysql:5.7 --lower-case-table-names=1 --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci