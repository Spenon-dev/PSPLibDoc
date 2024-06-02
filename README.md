# PSPLibDoc
An attempt to document symbols of PSP modules across all firmwares
<br>

## Usage
### Prerequisites
psp_libdoc.py and psp_print_libdoc.py require python3 with lxml module
Page with the current NID status for each library can be found [here](https://spenon-dev.github.io/PSPLibDoc/).

### Common psp_libdoc operations
 - Loading source files
    - Load one or more PSPLibDoc XML files
        - psp_libdoc.py -l input_1.xml input_2.xml input_3.xml...

    - Load one or more PSP export files
        - psp_libdoc.py -e input_1.exp input_2.exp input_3.exp...

    - Load one or more PPSSPP source files (HLEFunction arrays)
        - psp_libdoc.py -p input_1.cpp input_2.cpp input_3.cpp...

    - Combination of multiple different sources
        - psp_libdoc.py -l input_1.xml input_2.xml... -e input_1.exp input_2.exp... -p ...

 - Save a combined PSPLibDoc XML file from all loaded sources
    - psp_libdoc.py *sources* -c psp_libdoc.xml
    - save_combined.sh will create a combined PSPLibDoc file for all firmwares

 - Save PRX modules as individual PSPLibDoc XML files from all loaded sources
    - psp_libdoc.py *sources* -s outputFolder

 - Update a PSPLibDoc XML file with known NIDs from all loaded sources
    - psp_libdoc.py *sources* -u psp_libdoc_to_update.xml
    - update_imports.sh will update the Import files for all firmwares from the combined PSPLibDoc

 - Update the PSPLibDoc XML files of all firmwares from PSP export files (*.exp)
    - Put all export files into an input folder and name them after the prx it should update
    - Example: ata.exp, sysmem.exp in inputFolder will update ata.xml and sysmem.xml across all firmwares
    - ./update_from_psp_exports.sh inputFolder


 - Export all unknown NIDs from all loaded sources
    - psp_libdoc.py *sources* -o unknown_nids.txt

 - Export all known function names from all loaded sources
    - psp_libdoc.py *sources* -k known_function_names.txt
<br>

### Common psp_print_libdoc operations
 - Print all exports of a given PRX module
    - psp_print_libdoc.py -d *directory* -e *module*
    - Example: psp_print_libdoc.py -d PSPLibDoc/1.50/ -e sysmem

 - Print all imports of a given PRX module
    - psp_print_libdoc.py -d *directory* -i *module*
    - Example: psp_print_libdoc.py -d PSPLibDoc/1.50/ -i threadman

 - Print all PRX modules exporting a given library
    - psp_print_libdoc.py -d *directory* -l *library*
    - Example: psp_print_libdoc.py -d PSPLibDoc/1.50/ -l SysMemForKernel

 - Print all PRX modules importing a given library
    - psp_print_libdoc.py -d *directory* -m *library*
    - Example: psp_print_libdoc.py -d PSPLibDoc/1.50/ -m LoadCoreForKernel
<br>

## General Notes
 - psp_libdoc currently does not load or save variables (Updating a PSPLibDoc however preserves variables)
 - Updating a PSPLibDoc is based on NID only, a loaded entry with the same NID will overwrite the previous one
<br>

## Firmware Notes
 - Firmware 1.00 is an accidentally leaked pre-release firmware by Sony (also known as 1.00 Bogus)
 - Firmware 1.03 is the actual PSP Japan release firmware (VSH only reports 1.00)
 - Firmwares in the ePSPVitaLibDoc folder refer to PS Vita firmware
 - The PS Vita ePSP emulator was based on different PSP firmwares throughout its lifecycle
    - Since PS Vita ePSP 0.931 -> PSP 6.20
    - Since PS Vita ePSP 0.990 -> PSP 6.36
    - Since PS Vita ePSP 1.03 -> PSP 6.60
    - Since PS Vita ePSP 3.36 -> PSP 6.61
<br>

## Credits
A big thanks goes to
 - All original PSPLibDoc contributers
 - All PPSSPP contributers for additional user library symbols
 - All UOFW contributers for updated 6.60 and 6.61 symbols
 - artart78 for additional scripts and Github CI for NID status HTML page.
 - artart78, Draan, efonte, GrapheneCt, sajattack, SilverSpring, zecoxao for additional symbol sources and NIDs
