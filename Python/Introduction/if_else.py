#Author: Jennifer Cafiero
#HackerRank Python - If-Else

import sys


N = int(raw_input().strip())
if N%2 != 0 and N >=1:
    print "Weird"
elif N % 2 == 0 and N >= 2 and N <= 5:
    print "Not Weird"
elif N % 2 == 0 and N >= 6 and N <= 20:
    print "Weird"
else:
    print "Not Weird"
