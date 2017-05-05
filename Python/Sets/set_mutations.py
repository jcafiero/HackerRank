#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Set Mutations

a = int(input())
setA = set(list(map(int, input().split())))
n = int(input())
for i in range(n):
    cmd = input().split()
    op = cmd[0]
    s = set(list(map(int, input().split())))
    if op == 'intersection_update':
        setA.intersection_update(s)
    elif op == 'update':
        setA.update(s)
    elif op == 'symmetric_difference_update':
        setA.symmetric_difference_update(s)
    elif op == 'difference_update':
        setA.difference_update(s)

print(sum(setA))
