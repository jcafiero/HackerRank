#Author: Jennifer Cafiero
#Date: April 28, 2017
#HackerRank Python - Tuples

def main():
    n = int(input())
    int_list = map(int, input().split())
    list = [x for x in int_list]
    t = tuple(list)
    print(hash(t))

        
if __name__ == "__main__":
    main()
