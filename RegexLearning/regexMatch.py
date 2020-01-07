import re

def main():
    fh = open("regex-sample.txt").readlines()
    for lineString in fh :
         regexMatch = re.search('(Neverm|Len)ore' , lineString)
         if regexMatch :
            print (regexMatch.group())

if __name__=="__main__": main()