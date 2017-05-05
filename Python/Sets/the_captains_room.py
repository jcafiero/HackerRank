#Author: Jennifer Cafiero
#Date: May 5 2017
#HackerRank Python - The Captain's Room

K = int(input())
families = list(map(int, input().split()))
rooms = set(families)
print(int((sum(rooms) * K - sum(families))/(K - 1)))
