#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Set .add()

arr = set({})
N = int(input())
for _ in range(N):
    temp = input()
    arr.add(temp)
print(len(arr))
