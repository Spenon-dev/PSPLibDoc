#! /usr/bin/env python3

import argparse
import os
import sys

from collections import defaultdict
from lxml import etree as ET

prxFolders = ("kd", "vsh/module")

def loadPSPLibdoc(xmlFile, targetLibrary):
	tree = ET.parse(xmlFile)
	root = tree.getroot()

	nidEntries = defaultdict(set)
	for prx in root.findall("PRXFILES/PRXFILE"):
		prxFile = prx.find("PRX").text
		for library in prx.findall("LIBRARIES/LIBRARY"):
			libraryName = library.find("NAME").text
			if (libraryName == targetLibrary) or (not targetLibrary):
				for function in library.findall("FUNCTIONS/FUNCTION"):
					functionNID = function.find("NID").text.upper().removeprefix('0X')
					functionName = function.find("NAME").text
					nidEntries[prxFile].add( (libraryName, functionNID, functionName) )

	for prx in nidEntries.keys():
		nidEntries[prx] = sorted(nidEntries[prx], key = lambda x: (x[0], x[1]))

	return nidEntries

def loadPrxModule(directory, category, module, library):
	nidEntries = {}
	for prxFolder in prxFolders:
		filePath = directory + '/' + category + '/' + prxFolder + '/' + module + '.xml'
		if os.path.isfile(filePath):
			print("Loading NID entries from '{}' ...".format(filePath))
			nidEntries.update(loadPSPLibdoc(filePath, library))

	return nidEntries

def loadAllPrxModules(directory, category, library):
	nidEntries = {}
	for prxFolder in prxFolders:
		dirPath = directory + '/' + category + '/' + prxFolder + '/'
		for libdocFile in os.listdir(dirPath):
			filePath = os.path.join(dirPath, libdocFile)
			fileEntries = loadPSPLibdoc(filePath, library)

			if(len(fileEntries) > 0):
				print("Loading NID entries from '{}' ...".format(filePath))
				nidEntries.update(fileEntries)

	return nidEntries

def printPrxFunctions(entries):
	for prx in entries.keys():
		print(prx)
		currentLib = ""

		for entry in entries[prx]:
			if currentLib != entry[0]:
				if currentLib:
					print()

				currentLib = entry[0]
				print('\t' + currentLib)

			print('\t\t|-- ' + '0x' + entry[1] + " --> " + entry[2])
		print()

def printModuleExports(directory, module):
	exports = loadPrxModule(directory, "Export", module, "")

	if(len(exports) == 0):
		print("No exports found for module '{}'".format(module))
	else:
		print("\nExports for module '{}':".format(module))
		printPrxFunctions(exports)

def printModuleImports(directory, module):
	imports = loadPrxModule(directory, "Import", module, "")

	if(len(imports) == 0):
		print("No imports found for module '{}'".format(module))
	else:
		print("\nImports for module '{}':".format(module))
		printPrxFunctions(imports)

def printLibraryExports(directory, library):
	exports = loadAllPrxModules(directory, "Export", library)

	if(len(exports) == 0):
		print("No modules found exporting library '{}'".format(library))
	else:
		print("\nModules exporting library '{}':".format(library))
		printPrxFunctions(exports)

def printLibraryImports(directory, library):
	imports = loadAllPrxModules(directory, "Import", library)

	if(len(imports) == 0):
		print("No modules found importing library '{}'".format(library))
	else:
		print("\nModules importing library '{}':".format(library))
		printPrxFunctions(imports)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('-d', '--directory',
						required=True,
						type=str,
						help='Directory of the PSP-Libdoc XML folder')

	parser.add_argument('-e', '--exports',
						required=False,
						type=str,
						help='Print all exports of the specified PRX module')

	parser.add_argument('-i', '--imports',
						required=False,
						type=str,
						help='Print all imports of the specified PRX module')

	parser.add_argument('-l', '--libraryExports',
						required=False,
						type=str,
						help='Print all PRX modules exporting the specified library')

	parser.add_argument('-m', '--libraryImports',
						required=False,
						type=str,
						help='Print all PRX modules importing the specified library')

	args = parser.parse_args(sys.argv[1:])

	if(args.exports):
		printModuleExports(args.directory, args.exports)

	if(args.imports):
		printModuleImports(args.directory, args.imports)

	if(args.libraryExports):
		printLibraryExports(args.directory, args.libraryExports)

	if(args.libraryImports):
		printLibraryImports(args.directory, args.libraryImports)










