#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - What's Your Name?

def print_full_name(a, b):
    first = a
    last = b
    print ("Hello " + first +" " + last + "! You just delved into python.")

if __name__ == "__main__":
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
