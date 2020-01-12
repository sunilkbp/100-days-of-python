def main():
    try:
        for i in inclusiveRange():
            print (i, end=" ")
    except TypeError as e:
        print(e)

def inclusiveRange(*args):
    length=len(args)
    if length==0 :
        raise TypeError ("Invalid number of input passed atleast 1 argument required")
    elif length==1:
        start = 0
        (end,) = args
        step = 1
    elif length ==2:
        (start , end )= args
        step = 1
    elif length==3:
        (start,end,step) = args
    while(start<=end):
        yield start
        start += step

if __name__== "__main__": main()