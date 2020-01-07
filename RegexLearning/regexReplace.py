
# Simple String replace along with regex.
import re
def main():
    fh = open("regex-sample.txt").readlines()
    for lineString in fh :
         regexMatch = re.search('(Neverm|Len)ore' , lineString)
         # string  way of replacing stirng
         if regexMatch :
            newString = lineString.replace(regexMatch.group(), "###")
            print(newString)
         # Regex way of replacing
         if regexMatch :
            print (re.sub('(Neverm|Len)ore' ,"###" , lineString ))



if __name__=="__main__": main()