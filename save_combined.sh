#! /bin/bash

NID_REPOSITORIES=("PSPLibDoc" "PSPGoLibDoc" "ePSPVitaLibDoc")
PRX_FOLDERS=("kd" "vsh/module")

for REPOSITORY in ${NID_REPOSITORIES[@]}
do
    FIRMWARE_PATH="./${REPOSITORY}"
    for FIRMWARE in `ls -1 $FIRMWARE_PATH`
    do
        PRX_FILES=()
        for PRX_FOLDER in ${PRX_FOLDERS[@]}
        do
            PRX_PATH="./${REPOSITORY}/${FIRMWARE}/Export/${PRX_FOLDER}/"
            if [ -d "${PRX_PATH}" ]; then
                mapfile -t -O "${#PRX_FILES[@]}" PRX_FILES < <(ls -1 "${PRX_PATH}"*.xml)
            fi
        done

        COMBINED_LIBDOC_FILE="${REPOSITORY}_${FIRMWARE}.xml"
        echo "Saving combined PSP-Libdoc file ${COMBINED_LIBDOC_FILE}"
        ./psp_libdoc.py -l ${PRX_FILES[@]} -c "./${REPOSITORY}/${FIRMWARE}/${COMBINED_LIBDOC_FILE}"
    done
done


