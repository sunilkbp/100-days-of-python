
# Simple program for regex Syntax understanding.


import re

def main():
    fh = open("regex-sample.txt")
    for line in fh.readlines():
        match = re.search( '(Len|Neverm)ore', line)
        if(match):
            print(line, end="")

if __name__== "__main__": main()