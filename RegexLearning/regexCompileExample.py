
# Can you write a program using regex to hash the matched string ?

import re

def main():
    fh = open("regex-sample.txt")
    pattern = re.compile("(Neverm|Len)ore" , re.IGNORECASE)
    for line in fh :
        match = re.search(pattern,line)
        if match:
            print(re.sub(pattern,"###",line), end="")
            print(pattern.sub("###",line), end="")

if __name__=="__main__": main()