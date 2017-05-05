#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Set .intersection() Operation

n = int(input())
s1 = set(list(map(int, input().split())))
b = int(input())
s2 = set(list(map(int, input().split())))

s1_int_s2 = s1.intersection(s2)

print(len(s1_int_s2))
