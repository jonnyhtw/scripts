#!/Users/Jonny/miniconda3/bin/python/

import os
from tqdm import tqdm
from datetime import datetime
import shutil

#replace spaces with underscores
for f in tqdm(os.listdir(".")):

    if os.path.isfile(f):
        r = f.replace(" ", "_")
        if r != f:
            os.rename(f, r)

#assign date in file name
for f in tqdm(os.listdir(".")):

    date = datetime.now().isoformat()
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    if os.path.isfile(f):
        os.rename(f, str(date) + "-" + f)

#move to wireless hard drive
for f in tqdm(os.listdir(".")):
    if os.path.isfile(f):
        shutil.move(f, "/Volumes/Data/Pictures/")
