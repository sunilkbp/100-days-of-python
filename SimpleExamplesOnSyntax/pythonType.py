
# Can you explain Type of objects ?

def main():
    listOfValues = [1,2,"three","4", (1,2,4), {"a":1,"b":2},{"sunday","monday"}]
    for i in listOfValues:
        print("Value:", i , "Type:", type(i), "ID of:",id(i))
    print( "Type of dataStructure", type(listOfValues))

if __name__ == '__main__':main()