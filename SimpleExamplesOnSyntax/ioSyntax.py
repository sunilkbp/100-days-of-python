
# Learn simple IO syntax .

def main():
    fh = open('sample.txt')
    for i in fh.readlines():
        print(i, end="")
    print("done")


if __name__ == '__main__': main()
