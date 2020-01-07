
# Simple String replace along with regex.
import re
def main():
    fh = open("regex-sample.txt")
    pattern = re.compile("(Len|Neverm)ore", re.IGNORECASE)
    for line in fh:
        match = re.search(pattern, line)
        if match:
            print (re.sub(pattern, "###" , line))

if __name__=="__main__": main()