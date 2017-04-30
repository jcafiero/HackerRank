#Author: Jennifer Cafiero
#Date: April 28, 2017
#HackerRank Python - Nested Lists

def main():
    n = int(input())
    gradebook = {}
    for _ in range(n):
        name = input()
        score = float(input())
        if score in gradebook:
            gradebook[score].append(name)
        else:
            gradebook[score] = [name]
    gradebook.pop(min(gradebook))
    answer = gradebook[min(gradebook)][:]
    answer.sort()
    for name in answer:
        print(name)

        

if __name__ == "__main__":
    main()
