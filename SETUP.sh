#!/bin/bash
###############################################################
# This script will ensure that the PYTHONPATH ENV 
# Variable contains the root of the project so scripts that are
# executed with this SETUP can always find packages installed
# at the root of the library.
###############################################################

DIR="$(cd "$(dirname "$0")" && pwd)"

#echo "Before: $PYTHONPATH"

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

#echo "After: $PYTHONPATH"


