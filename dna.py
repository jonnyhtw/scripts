#!/usr/bin/env python
import argparse 


import mmap

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, type=str)
args = parser.parse_args()

file=args.file
print('file is', file)

i = 0

with open(file) as f:


    new_list = []
    concat = False
    for line in tqdm(f, total=get_num_lines(file)):
        if line.startswith('>'):
            new_list.append('>'+line[line.find('Eukaryota'):].replace('\n',''))
        if set(line.strip()) == {'A', 'C', 'G', 'T'}:
            if concat:
                new_list[-1] += line.strip()
            else:
                new_list.append(line.strip())
            concat = True
        else:
            concat = False

file = open(file+'-edited.txt','w')
for item in new_list:
    file.write(item+"\n")
file.close()


