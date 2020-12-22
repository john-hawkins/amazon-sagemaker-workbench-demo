#!/bin/sh
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

PREP="false"
PROCESS="false"
MODEL="false"

for var in "$*"; do
        case $var in

                prepare)
                        PREP="true"
                        ;;

                process)
                        PROCESS="true"
                        ;;

                model)
                        MODEL="true"
                        ;;

                all)
                        PREP="true"
                        PROCESS="true"
                        MODEL="true"
                        ;;

                help)
                        echo "Usage:"
                        echo "$0 (prepare|process|model|all|help) "
                        echo ""
                        echo "   prepare     To download data and unzip data"
                        echo "   process     To run the global processing script"
                        echo "   model       To run the set of models configured in experiment"
                        echo "   all         To run all of the above"
                        echo "   help        To view the help"
                        exit 0
                        ;;
        esac
done

if [ $PREP = "true" ]
then
        echo "Preparing your data...";
        src/prepare_data.sh data
        echo "Done.\n";
fi

if [ $PROCESS = "true" ]
then
        echo "Processing your data...";
        src/process_data.sh
        echo "Done.\n";
fi

if [ $MODEL = "true" ]
then
        echo "Modelling your data...";
        echo "Done.\n";
fi
