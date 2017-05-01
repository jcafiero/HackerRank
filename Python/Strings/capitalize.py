#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - Capitalize!

def capitalize(string):
    return " ".join(map(lambda x:x.capitalize(),string.split(" ")))


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
