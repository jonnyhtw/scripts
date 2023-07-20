#!/Users/Jonny/miniconda3/bin/python/

import os
from tqdm import tqdm
from datetime import datetime
import shutil



for f in tqdm(os.listdir(".")):

    r = f.replace(" ","_")
    if( r != f):
        os.rename(f,r)

for f in tqdm(os.listdir(".")):

    date = datetime.now().isoformat()
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    os.rename(f,str(date)+'-'+f)

for f in tqdm(os.listdir(".")):
    shutil.move(f,'/Volumes/Data/Pictures')
