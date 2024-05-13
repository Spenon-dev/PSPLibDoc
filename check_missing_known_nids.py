#! /usr/bin/env python3

import psp_libdoc
import glob
from collections import defaultdict

all_nids = defaultdict(set)
all_unk_nids = []

filelist = glob.glob('*PSP*/*/Export/**/*.xml', recursive=True)
for (idx, file) in enumerate(filelist):
    entries = psp_libdoc.loadPSPLibdoc(file)
    version = file.split('/')[1]
    moduleName = file.split('/')[-1].split('.')[0] + '.prx'
    for e in entries:
        if psp_libdoc.compute_nid(e.name) == e.nid:
            all_nids[e.nid].add((e.name, moduleName, e.libraryName))
        else:
            all_unk_nids.append((e.nid, e.name, moduleName, e.libraryName))

for (nid, name, mod, lib) in all_unk_nids:
    if nid in all_nids:
        if len(set([x[0] for x in all_nids[nid]])) > 1:
            print("WARN: collision in NIDs?", nid, mod, lib, all_nids[nid])
        else:
            (name2, mod2, lib2) = list(all_nids[nid])[0]
            print(f"XXX [{mod}.{lib}/{mod2}.{lib2}: s/{name}/{name2}/")

