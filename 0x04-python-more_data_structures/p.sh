#!/bin/bash

for item in $(find *.py)
do
  echo "#!/usr/bin/python3" > $item;
done
