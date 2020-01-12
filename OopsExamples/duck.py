
class Duck():
    def __init__(self, value=15):
        print ("Constructor")
        self._value = value

    def walk (self):
        print ("Duck walks like a duck",self._value)
    def getValue(self):
        return self._value

def main():
    donald = Duck(10)
    jim = Duck()
    donald.walk()
    print( "Class Donald :", donald.getValue())
    jim.walk()
    print("Class jim :", jim.getValue())
    print (type(donald), type(jim))
if __name__=="__main__":main()