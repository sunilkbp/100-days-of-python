
# Learn simple IO syntax, with argument defaults.

def main():
    #Test function explains simple arguments
    testFunc(5, 10, "abc")
    testFunc(6, "abc")
    testFunc(3)

    #Test function explains list of arguments
    testFunc2(1,2,3,4,5,6)
    testFunc2(1, 2 )

    # testFunc3 Keyword arguments.
    testFunc3(1,2,3,4,5,6, kw1=7, kw2=8, kw3=9 )

def testFunc(x, y=None ,z=3):
    if y is None : y=100
    print ("Input values", x, y,z)

def testFunc2(x,y,z=None,*args):
    print(type(args))
    try:
        print("Values of Argument passsed :", x, y, z, args[0], args[1],args[2])
    except IndexError as e:
        print ("Argument index is empty")

def testFunc3(x,y,z,*args,**kwargs):
    print (x,y,z, args, kwargs)
    print (type(args),type(kwargs))
    for key in kwargs.keys():
        print("value of dict element {}, is {}".format(key, kwargs.get(key,None)))


    #print (type(*args),type(**kwargs))


if __name__ == '__main__': main()
