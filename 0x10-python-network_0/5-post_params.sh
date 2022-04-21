#!/bin/bash
# send a POST and display size of body responce 
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"