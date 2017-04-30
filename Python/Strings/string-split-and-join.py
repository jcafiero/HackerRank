#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - String Split & Join

def split_and_join(line):
    temp = line.split(" ")
    temp = "-".join(temp)
    return temp


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
