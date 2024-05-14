#! /usr/bin/env python3

# Finds all the names from all the XML files which match their NID, and sees if the NID is unattributed (or incorrectly attributed) somewhere else

import psp_libdoc
import glob
from collections import defaultdict

# For each NID with a confirmed name, holds the (name, module, library) tuples
all_nids = defaultdict(set)
# List of (NID, name, module, library) tuples with non-matching or unknown NID
all_unk_nids = []

# Browse all the export files
filelist = glob.glob('*PSP*/*/Export/**/*.xml', recursive=True)
for (idx, file) in enumerate(filelist):
    entries = psp_libdoc.loadPSPLibdoc(file)
    # Get the version and module name from the path
    version = file.split('/')[1]
    moduleName = file.split('/')[-1].split('.')[0] + '.prx'
    for e in entries:
        # Check if the specified names match their NID
        if psp_libdoc.compute_nid(e.name) == e.nid:
            all_nids[e.nid].add((e.name, moduleName, e.libraryName))
        else:
            all_unk_nids.append((e.nid, e.name, moduleName, e.libraryName))

# Check, for all unknown NIDs, correct NIDs which would match
for (nid, name, mod, lib) in all_unk_nids:
    if nid in all_nids:
        if len(set([x[0] for x in all_nids[nid]])) > 1:
            print("WARN: collision in NIDs?", nid, mod, lib, all_nids[nid])
        else:
            (name2, mod2, lib2) = list(all_nids[nid])[0]
            print(f"XXX [{mod}.{lib}/{mod2}.{lib2}: s/{name}/{name2}/")

