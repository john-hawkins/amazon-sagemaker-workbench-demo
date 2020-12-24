#!/bin/bash
##############################################################################
# Master RUN script.
# To execute all components of the demo without using Jupyter.
#
##############################################################################

LOAD="false"
PROCESS="false"
PARTITION="false"
STORE="false"
MODEL="false"
HELP="false"
CLEAN="false"

if [ $# -eq 0 ]
then
        echo ""
        echo "Command Switch Required."
        echo ""
        HELP="true"
fi


for var in "$*"; do
        case $var in

                load)
                        LOAD="true"
                        ;;

                process)
                        PROCESS="true"
                        ;;

                partition)
                        PARTITION="true"
                        ;;

                store)
                        STORE="true"
                        ;;

                prepare)
                        LOAD="true"
                        PROCESS="true"
                        PARTITION="true"
                        STORE="true"
                        ;;

                model)
                        MODEL="true"
                        ;;

                all)
                        LOAD="true"
                        PROCESS="true"
                        PARTITION="true"
                        STORE="true"
                        MODEL="true"
                        ;;

                help)
                        HELP="true"
                        ;;

                clean)
                        CLEAN="true"
                        ;;

        esac
done

######################################################################
# ENSURE THAT THE SCRIPT IS ALWAYS EXECUTED FROM ITS LOCATION 
# AND THAT PYTHON CAN FIND LOCAL PACKAGES
######################################################################
DIR="$(cd "$(dirname "$0")" && pwd)"
cd $DIR

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

######################################################################
# EXECUTE THE REQUIRED STEPS 
######################################################################

if [ $LOAD = "true" ]
then
        echo "Loading your data...";
        src/load_data.sh data
        echo "Done.";
fi

if [ $PROCESS = "true" ]
then
        echo "Processing your data...";
        python3 src/process_data.py
        echo "Done.";
fi

if [ $PARTITION = "true" ]
then
        echo "Partitioning your data...";
        python3 src/partition_data.py
        echo "Done.";
fi

if [ $STORE = "true" ]
then
        echo "Storing your data to S3...";
        python3 src/store_data.py
        echo "Done.";
fi

if [ $MODEL = "true" ]
then
        echo "Modelling your data...";

        while read model script
        do
            echo "$model: $script"
            python3 experiments/$(echo $script)
        done < experiments/model_list.config

        echo "Done.";
fi


if [ $CLEAN = "true" ]
then
        echo "Cleaning your endpoints... ";
        echo "TODO...";
fi

if [ $HELP = "true" ]
then
   echo "  USAGE"
   echo "  -----------------------------------------------------------------"
   echo "  $0 (load|process|partition|store|prepare|model|all|clean) "
   echo ""
   echo "    load        To download and unzip raw data"
   echo "    process     To run the global processing script"
   echo "    partition   To partition the data for training and testing."
   echo "    store       To store the partitioned data into S3"
   echo "    prepare     Perform all prep steps: LOAD,PROCESS,PARTITION,STORE"
   echo "    model       To run the set of models configured in experiment"
   echo "    all         To run all of the above"
   echo "    clean       Clean up the endpoints"
   echo ""
fi

