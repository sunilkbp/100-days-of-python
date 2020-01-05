
# Syntax and accessing Dictorary Object ?
def main():

    maxTemp = { "mon" : 20, "tue" : 25 , "wed" : 22 , "thr" : 18 , "fri" : 18 , "sat" : "23" , "sun" : 19}
    print("***** Printing Dict 1 *****")
    for day in maxTemp.keys():
        print ("On {} day, max temp reached in bangalore is {}".format(day , maxTemp.get(day)))

    print("**** Printing Dict 2 ****")
    maxTemp2 = dict( mon = 20, tue = 25 , wed = 22 , thr = 18 , fri = 18 , sat = "23" , sun = 19)
    for day in sorted(maxTemp2.keys()):
        print ("On {} day, max temp reached in bangalore is {}".format(day , maxTemp2[day]))

if __name__ == '__main__':main()