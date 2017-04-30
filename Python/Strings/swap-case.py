#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - sWAP cASE

def swap_case(s):
    temp = ""
    for char in s:
        if char.islower():
            temp += char.upper()
        else:
            temp += char.lower()
    return temp


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
