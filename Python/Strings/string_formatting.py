#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - String Formatting

def print_formatted(number):
    l = len(bin(number))-1
    for i in range(1,number+1):
        print(str(i).rjust(l-1)+oct(i)[2:].rjust(l)+hex(i)[2:].upper().rjust(l)+bin(i)[2:].rjust(l))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
