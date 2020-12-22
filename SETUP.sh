#!/bin/bash
######################################################
# This script will ensure that the PYTHON PATH ENV 
# Variable contains the root of the project so scripts
# can find the utils library.
######################################################

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Before: $PYTHONPATH"

if [[ -z "${PYTHONPATH}" ]]; then
  export PYTHONPATH="$DIR"

else
  echo $PYTHONPATH | grep -q "$DIR"

  if [ $? -eq 0 ]; then
    export PYTHONPATH="$PYTHONPATH:$DIR"
  else
    export PYTHONPATH
  fi

fi

echo "After: $PYTHONPATH"


