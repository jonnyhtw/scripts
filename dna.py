#!/usr/bin/env python
import argparse
import mmap

try:
    from tqdm import tqdm

    _tqdm = True
    print("The tqdm progress bar software is available in this version of Python.")
except ImportError:
    _tqdm = False
    print("The tqdm progress bar software is not available in this version of Python.")


def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines


parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, type=str)
args = parser.parse_args()

file = args.file
print("file is", file)

with open(file) as f:

    new_list = []
    concat = False
    if _tqdm:
        my_iterator = tqdm(f, total=get_num_lines(file))
    else:
        my_iterator = f

    for line in my_iterator:
        if line.startswith(">"):
            new_list.append(
                            ">" + line[line.find("Eukaryota") :].
                            replace("\n", ";").
                            replace('phylum_class_order_family_genus_','').
                            replace('class_order_family_genus_','').
                            replace('order_family_genus_','').
                            replace('family_genus_','').
                            replace('genus_','')
                            )
        if set(line.strip()) == {"A", "C", "G", "T"}:
            if concat:
                new_list[-1] += line.strip()
            else:
                new_list.append(line.strip())
            concat = True
        else:
            concat = False

file = open(file + "-edited.txt", "w")
for item in new_list:
    file.write(item + "\n")
file.close()
