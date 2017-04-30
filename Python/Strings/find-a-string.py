#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - Find a String

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
