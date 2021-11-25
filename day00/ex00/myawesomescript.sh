#!/bin/sh
url=$1
if [ $url ]; then
  curl -si $1 | grep "location: " |  cut -d ' ' -f 2-
fi
