
#  Write one simple Class example of Egg ? and explain OOPS in it.

class Egg:
    def __init__(self, type="fried"):
        self._type = type
    def getEgg(self):
        return self._type

def main():
    egg1=Egg("scrambled egg")
    whatKind = egg1.getEgg()
    print("egg is of type {}".format(whatKind))

    egg2 = Egg()
    whatKind = egg2.getEgg()
    print("egg is of type {}".format(whatKind))

if __name__=="__main__":main()