def main():
    rangeFunc(5)
    rangeFunc(10)

def rangeFunc( x = 0):
    for i in range(x):
        print (i, end=" ")
    print("")

if __name__ == "__main__" : main()