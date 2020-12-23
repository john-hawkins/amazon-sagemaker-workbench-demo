#!/bin/bash
##############################################################################
# Master RUN script.
# To execute all components of the demo without using Jupyter.
#
##############################################################################


if [ $# -eq 0 ]
then
        echo "CL Parameters are mandatory. We need to know which part to run."
        echo "  (run $0 -h for help)"
        echo ""
        exit 0
fi

LOAD="false"
PROCESS="false"
PARTITION="false"
STORE="false"
MODEL="false"

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
                        echo " USAGE"
                        echo "-------------------------------------------------"
                        echo "$0 (load|process|partition|store|prepare|model|all|help) "
                        echo ""
                        echo "   load        To download and unzip raw data"
                        echo "   process     To run the global processing script"
                        echo "   partition   To partition the data for training and testing."
                        echo "   store       To store the partitioned data into S3"
                        echo "   prepare     Perform all of the above steps: LOAD,PROCESS,PARTITION,STORE"
                        echo "   model       To run the set of models configured in experiment"
                        echo "   all         To run all of the above"
                        echo "   help        To view the help"
                        echo ""
                        exit 0
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
        echo "Done.\n";
fi

if [ $PROCESS = "true" ]
then
        echo "Processing your data...";
        python src/process_data.py
        echo "Done.\n";
fi

if [ $PARTITION = "true" ]
then
        echo "Partitioning your data...";
        python src/partition_data.py
        echo "Done.\n";
fi

if [ $STORE = "true" ]
then
        echo "Storing your data to S3...";
        python src/store_data.py
        echo "Done.\n";
fi

if [ $MODEL = "true" ]
then
        echo "Modelling your data...";

        while read model script
        do
            echo "$model: $script"
            python experiments/$(echo $script)
        done < experiments/model_list.config

        echo "Done.\n";
fi
