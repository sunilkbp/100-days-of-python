
# class to explain getter and setter methods.

class Duck():
    def __init__(self, color="red"):
        self._color = color

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color

    def quack(self):
        print ("Sounds like Quaack")

    def walk(self):
        print("Duck walks")

def main():
    print ("Class Duck creation and its method")
    donald = Duck()
    print(donald.getColor())
    donald.setColor("white")
    print(donald.getColor())
    donald.quack()
    donald.walk()

if __name__=="__main__":main()