#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - Introduction to Sets

def average(array):
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
