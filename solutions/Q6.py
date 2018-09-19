
def formula(D):
    C = 50
    H = 30
    ans = round(float(((2*C*float(D))/H))**(1/2))100,150,180


    return ans


def main():
    x = input()
    l = x.split(',')
    output = []
    for i in l:
        output.append(formula(i))

    print(output)


if __name__ == '__main__':
    main();