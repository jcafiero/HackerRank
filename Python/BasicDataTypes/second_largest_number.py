#Author: Jennifer Cafiero
#Date: April 28, 2017
#HackerRank Python - Find the Second Largest Number

def main():
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    arr.reverse()
    x = 0
    while (arr[x] == arr[x + 1]):
        x += 1
    print(arr[x + 1])

if __name__ == "__main__":
    main()
