#!/bin/bash
# display size of body responce 
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'