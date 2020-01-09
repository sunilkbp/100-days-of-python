
# Write a program to check file type and raise exception.

def main():
    try:
        readFileType("sample2.txt2")
    except ValueError as e:
        print("Error is Observed related to file Type" ,e)

def readFileType(fileName):
    if fileName.endswith("txt"):
        print ("File Type is valid")
    else :
        raise ValueError("filetype should be .txt")


if __name__=="__main__":main()