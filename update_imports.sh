#! /bin/bash

NID_REPOSITORIES=("PSPLibDoc" "PSPGoLibDoc" "ePSPVitaLibDoc")
PRX_FOLDERS=("kd" "vsh/module")

for REPOSITORY in ${NID_REPOSITORIES[@]}
do
    FIRMWARE_PATH="./${REPOSITORY}"
    for FIRMWARE in `ls -1 $FIRMWARE_PATH`
    do
        COMBINED_LIBDOC_FILE="${REPOSITORY}_${FIRMWARE}.xml"
        COMBINED_LIBDOC_PATH="./${REPOSITORY}/${FIRMWARE}/${COMBINED_LIBDOC_FILE}"

        if [ -f "${COMBINED_LIBDOC_PATH}" ]; then
            for PRX_FOLDER in ${PRX_FOLDERS[@]}
            do
                PRX_PATH="./${REPOSITORY}/${FIRMWARE}/Import/${PRX_FOLDER}/"

                if [ -d "${PRX_PATH}" ]; then
                    for PRX in `ls -1 "${PRX_PATH}"*.xml`
                    do
                        echo "Updating ${PRX}"
                        ./psp_libdoc.py -l "${COMBINED_LIBDOC_PATH}" -u "${PRX}"
                    done

                    echo ""
                fi
            done
        else
            echo "PSP-Libdoc ${COMBINED_LIBDOC_FILE} not found"
        fi
    done
done


