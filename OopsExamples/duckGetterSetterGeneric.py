
# class to explain getter and setter methods.

class Duck():
    def __init__(self, **kwargs):
        self.variables = kwargs

    def setVariable(self, key, value):
        self.variables[key]= value

    def getVariable(self,key):
        return self.variables.get(key, None)

    def quack(self):
        print ("Sounds like Quaack")

    def walk(self):
        print("Duck walks")

def main():
    print ("Class Duck creation and its method")
    donald = Duck()
    donald.setVariable("color", "red")
    print ("Duck color is ", donald.getVariable("color"))
    dict1 = { "color" :"white", "legs" : 2 , "breed": "indian"}
    print(type(dict1))
    don = Duck(color ="white", legs = 2 , breed = "indian")
    print("Indian Duck :", don.getVariable("color"), don.getVariable("legs"), don.getVariable("breed"))
    don.setVariable("breed", "Irani")
    print("Imported Irani Duck  :", don.getVariable("color"), don.getVariable("legs"), don.getVariable("breed"))

if __name__=="__main__":main()