
def count(x):
    lowCount =0
    upCount = 0
    for i in x:
        if str(i).isupper() :
            upCount+=1
        elif str(i).islower() :
            lowCount+=1

    return lowCount,upCount

def main():
    x = str(input())

    lowCount,upCount =count(x)
    print("UPPER CASE ",upCount)
    print("LOWER COUNT ",lowCount)
    pass

if __name__=="__main__":
    main()