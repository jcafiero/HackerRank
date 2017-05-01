#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - Alphabet Rangoli

def print_rangoli(size):
    ret = []
    for i in range(size -1, -1, -1):
        ret.append(chr(ord('a') + i))
        print("-".join(ret[:-1] + ret[-1::-1]).center(4 * size - 3, "-"))
    for i in range(0, size-1, 1):
        ret.remove(chr(ord('a') + i))
        print("-".join(ret[:-1] + ret[-1::-1]).center(4 * size - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
