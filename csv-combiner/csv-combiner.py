import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path", nargs="+")
args = parser.parse_args()
file_paths = [ os.path.abspath(path) for path in args.csv_file_path ] # get absolute path for each arg passed in


def read_print_file(path):
    with open(path, "r") as f:
        file_name = path.split('/')[-1]
        lines = f.read().splitlines()[1:] # get rid of header
        for line in lines:
            print(f'{line},"{file_name}"')


print('"email_hash","category"')
for path in file_paths:
    # read individual file here
    # data ==> dict{ email_hash : category }
    read_print_file(path)
