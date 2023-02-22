import os
import numpy as np
import json
import simmer

with open('II_perspective.txt', 'r') as results_file :
    filedata = results_file.read()
    runslice = filedata.split('"timeout":false,"failed_images":[],"failed_audio":[],"failed_video":[]')
    subs = []
    for partinum in range(len(runslice)-1):
        with open('results.txt','w') as f:
            f.write(runslice[partinum+1])
            current_run = simmer.simmer()
            subs+=[current_run]
            print(current_run['ID'])

with open("summary.json", "w") as write_file:
    json.dump(subs, write_file, indent=4)
            