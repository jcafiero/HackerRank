#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - Designer Door Mat

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print ((((M // 2) - (( i * 3) // 2)) * "-") + (i * ".|.") + (((M // 2) - ((i * 3) // 2)) * "-"))
print ((((M // 2) - 3) * "-") + "WELCOME" + (((M // 2) - 3) * "-"))
for i in range(N-2,-1,-2): 
    print ((((M // 2) - ((i * 3) // 2)) * "-") + (i *".|.") + (((M // 2) - ((i *3) // 2)) * "-"))


    
