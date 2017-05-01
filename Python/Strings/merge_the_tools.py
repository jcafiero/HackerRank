#Author: Jennifer Cafiero
#Date: May 1 2017
#HackerRank Python - Merge the Tools

def merge_the_tools(string, k):
    substrings = [string[i:i + k] for i in range(0, len(string), k)]
    for sub in substrings:
        s = sub[0]
        for i in range(1, len(sub)):
            if sub[i] not in sub[:i]:
                s += sub[i]
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
