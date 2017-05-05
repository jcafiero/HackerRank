#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - Check Subset

for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    print(True) if (A&B == A) else print(False)
