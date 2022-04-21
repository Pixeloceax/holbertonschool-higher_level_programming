#!/bin/bash
#send a GET and display size of body responce s
curl -s "$1" -X GET -H "X-School-User-Id: 98"
