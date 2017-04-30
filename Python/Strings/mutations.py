#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - Mutations

def mutate_string(string, position, character):
    temp = list(string)
    temp[position] = character
    rejoin = ''.join(temp)
    return rejoin



if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
