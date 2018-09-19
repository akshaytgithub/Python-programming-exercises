
class Q5 :

    def __init__(self):
        self.x = ""


    def getString(self):
        self.x = input()
        return self.x
    def printString(self):
        print(self.x.upper())

def main():
    ob = Q5()
    ob.getString()
    ob.printString()
    pass

if __name__ == '__main__':
    main()
