#Author: Jennifer Cafiero
#Date: April 28, 2017
#HackerRank Python - List Comprehensions

def main():
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    print ([[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N])

if __name__ == "__main__":
    main()
