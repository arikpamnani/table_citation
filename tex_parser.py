import argparse
import json
import os
import re
import tarfile


def convert_gz_to_tar(path):
    for filename in os.listdir(path):
        if(filename.endswith(".gz")):
            old_path = os.path.join(path, filename)
            new_path = os.path.join(path, filename[:-3] + ".tar")
            os.rename(old_path, new_path)
    print("All .gz files converted to .tar")


def extract_tar(path):
    total_files = 0
    files_not_extracted = 0
    for filename in os.listdir(path):
        if(filename.endswith(".tar")):
            try:
                tar = tarfile.open(os.path.join(path, filename))
                tar.extractall(os.path.join(path, filename[:-4]))
                tar.close()
            except(Exception):
                files_not_extracted += 1
        total_files += 1
    print("Total files - %d"%total_files)
    print("Files not extracted - %d"%files_not_extracted)


def parse_tex(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        if(os.path.isdir(full_filename)):  
            for filename_ in os.listdir(full_filename):        
                if(filename_.endswith(".tex")):
                    full_filename_ = os.path.join(full_filename, filename_)
                    num_tables = find_tables(full_filename_)
                    print(filename, num_tables)


def find_tables(path):
    contents = ""
    num_tables = 0
    with open(path, 'r', encoding='ISO-8859-1') as fin:
        for line in fin:
            contents += (line)
            # if("\\begin{table}" in line or "\\begin{tabular}" in line):
                # print(line)
                # num_tables += 1
    # return num_tables
    result = []
    index = 0
    while(index < len(contents)):
        index = contents.find("\\begin{table}", index)
        index_ = contents.find("\\end{table}", index)
        result.append(contents[index:index_+len("\\end{table}")])
        if(index == -1):
            break
        index += 2
    num_tables = 0
    for k in result:
        if("\\begin{tabular}" in k):
            num_tables += 1
    return num_tables


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-config", required=True)
    args = parser.parse_args()
    
    with open(args.config) as configfile:
        config = json.load(configfile)
    
    src_path = config["src_path"]

    # convert_gz_to_tar(src_path)
    # extract_tar(src_path)
    parse_tex(src_path)
<<<<<<< HEAD
    # find_tables("D:\\arXiv_src_0812_004\\0812\\0812.4333\\tail_v3.tex")
=======
>>>>>>> a344dd1d25c64412547b7f4d41f547ab96163f4b
