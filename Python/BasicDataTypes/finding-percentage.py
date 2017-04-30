#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - Finding the percentage

def main():
    n = int(input())
    student_marks = {}
    for x in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_scores = student_marks[query_name]
    print("%.2f" % (sum(query_scores)/len(query_scores)))

if __name__ == "__main__":
    main()
