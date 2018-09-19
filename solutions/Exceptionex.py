import sys
def compute():
    try :
        x  = 5/0
    except Exception as e :
        print("Exception occured")
        print(sys.exc_info())
        print("Hello world")

def main():
    compute()
    print("Hello main")
    pass


if __name__ == '__main__':
    main()