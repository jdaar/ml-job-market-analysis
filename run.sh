#!/bin/bash
paths=$(ls /data | grep "\.csv$" | awk '{print "/data/"$1}')
lines=$(awk '$1 !~ /url,visited,platform,uuid/ { printf "%s ", $1 }' $paths)
parallel -j4 poetry run python -m market_analysis --line {} ::: $lines