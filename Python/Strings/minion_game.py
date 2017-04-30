#Author: Jennifer Cafiero
#Date: April 30 2017
#HackerRank Python - The Minion Game

def minion_game(string):
    stu = 0
    kev = 0
    count = 0
    for i in string:
        if i in "AEIOU":
            kev += len(string) - count
        else:
            stu += len(string) - count
        count += 1
    if kev == stu:
        print("Draw")
    elif kev > stu:
        print("Kevin", kev)
    else:
        print("Stuart", stu)



if __name__ == '__main__':
    s = input()
    minion_game(s)
