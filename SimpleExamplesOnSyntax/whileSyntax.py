
# Fibonacci seris example using while

def main():
    (a , b) = (0, 1)
    while a<=100:
        print (a, end=" ")
        (a, b) = (b, a+b)

if __name__ == '__main__': main()
