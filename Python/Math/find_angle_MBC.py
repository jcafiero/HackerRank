# Author: Jennifer Cafiero
#Date: April 30 2017
#HackerRank Python - Find Angle MBC

import math

ab = float(input())
bc = float(input())
tangent = ab/bc
tan_inv = math.atan(tangent)
ang = math.degrees(tan_inv)
print (str(int(round(ang, 0))) + '°')
