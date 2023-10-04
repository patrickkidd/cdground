#!/bin/bash -e

mkdir -p output
echo "`date`" >> output/buffer

echo "New contents:"
cat output/buffer
echo "Done"

