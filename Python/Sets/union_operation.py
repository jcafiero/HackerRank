#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Set .union() Operation

n = int(input())
s1 = set(list(map(int, input().split())))
m = int(input())
s2 = set(list(map(int, input().split())))

print (len(s1.union(s2)))
