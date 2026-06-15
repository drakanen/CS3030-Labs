import re, argparse

def read_log_lines(filepath, keyword):
    pattern = rf".*{re.escape(keyword)}.*"
    with open(filepath, "r") as f:
        for line in f:
            if re.search(pattern, line):
                yield line.strip()

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='The path of the file'
                                   ' you wish to search in', required=True)  # Location to search in
parser.add_argument('--keyword', help='The keyword to search for', required=True)  # Keyword to search for
args = parser.parse_args()

for line in read_log_lines(args.path, args.keyword):
    print(line)


    # f.read() loads the entire file into RAM at once
    # yield loads one line at a time
    # This can lead to f.read() crashing a system due to overloading the RAM capacity
    # Searching for a term in f.read() requires the entire log to be read
    # Searching in yield will stop reading once it is found