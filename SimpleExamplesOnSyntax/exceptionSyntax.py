
def main():
    try:
        fh = open("sample2.txt")
        for line in fh:
            print(line, end="")
    except IOError as e  :
        print ("IO error is noted", e)
    else:
        print ("\n\nNo exception, all is well..:)")



if __name__=="__main__":main()