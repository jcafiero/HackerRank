#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - No Idea!

n, m = map(int, (input().split(' ')))
arr = list(map(int, input().split(' ')))
A = set(list(map(int, input().split(' '))))
B = set(list(map(int, input().split(' '))))

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
        
print(happiness)
