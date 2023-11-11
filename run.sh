#!/bin/bash
paths=$(ls /data | cat | grep "\.csv$" | awk '{print "/data/"$1}')
lines=$(awk '$1 !~ /url,visited,platform,uuid/ { printf "%s ", $1 }' $paths)
parallel -j4 poetry run python /app/main.py --line {} ::: $lines