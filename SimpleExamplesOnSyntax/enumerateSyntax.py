# Enumeration example:

def main():
    str = "this is simple string"
    for i,c in enumerate(str) :
        if (c == "s"):
            continue
            print ("value of index {} : {}".format(i,c))
        print(c, end="")

if __name__== '__main__' : main()