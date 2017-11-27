from copy import deepcopy as dc

def semi_reversed_packing(number):

    former = list(i + 1 for i in range(int(number)))
    reversed_former = dc(former)
    reversed_former.reverse()
    new = list()

    for i in range(len(former)):
        new.append(former[i])
        new.append(reversed_former[i])
        new = new[:len(former)]
    return new

if __name__ == '__main__':
    N = (int(input("Введите размер N: ")))
    print(semi_reversed_packing(N))