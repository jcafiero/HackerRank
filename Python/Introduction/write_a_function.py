#Author: Jennifer Cafiero
#HackerRank Python - Write a function

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
                return leap
            leap = False
            return leap
        leap = True    
        return leap

    
    return leap
