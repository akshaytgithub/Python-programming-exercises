import re


def check(x):
    alpha = "[a-zA-Z]"
    num = "[0-9]"
    spe = "[$#@]"
    if len(x) >= 6 and len(x) <= 12:
        if re.search(alpha,str(x)):
            if re.search(num, str(x)):
                if re.search(spe, str(x)):
                    return True
    return False



def main():
    x = str(input()).split(",")
    for i in x:
        if check(i):
            print(i)

if __name__ == '__main__':
    main()