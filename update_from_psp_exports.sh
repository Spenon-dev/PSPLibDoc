#! /bin/bash

NID_REPOSITORIES=("PSPLibDoc" "PSPGoLibDoc" "ePSPVitaLibDoc")
PRX_FOLDERS=("kd" "vsh/module")

if [[ $# -ne 1 ]]; then
    echo "Usage: ${0} [input-path]"
    exit 1
fi

EXPORT_PATH="$1"

for EXPORT in `ls -1 $EXPORT_PATH`
do
    PRX_MODULE=${EXPORT%%.exp}
    for REPOSITORY in ${NID_REPOSITORIES[@]}
    do
        FIRMWARE_PATH="./${REPOSITORY}"
        for FIRMWARE in `ls $FIRMWARE_PATH`
        do
            for PRX_FOLDER in ${PRX_FOLDERS[@]}
            do
                PRX_PATH="${FIRMWARE_PATH}/${FIRMWARE}/Export/${PRX_FOLDER}/${PRX_MODULE}.xml"
                if [ -f "${PRX_PATH}" ]; then
                    echo "Updating Repository: ${REPOSITORY} Firmware: ${FIRMWARE} PRX: ${PRX_MODULE}"
                    psp_libdoc.py -e "${EXPORT_PATH}/${EXPORT}" -u "${PRX_PATH}"
                    echo ""
                fi

                PRX_PATH_KERMIT="${FIRMWARE_PATH}/${FIRMWARE}/Export/${PRX_FOLDER}/kermit_${PRX_MODULE}.xml"
                if [ -f "${PRX_PATH_KERMIT}" ]; then
                    echo "Updating Repository: ${REPOSITORY} Firmware: ${FIRMWARE} PRX: kermit_${PRX_MODULE}"
                    psp_libdoc.py -e "${EXPORT_PATH}/${EXPORT}" -u "${PRX_PATH_KERMIT}"
                    echo ""
                fi
            done
        done
    done
done


