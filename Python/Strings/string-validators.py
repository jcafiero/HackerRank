#Author: Jennifer Cafiero
#Date: April 30, 2017
#HackerRank Python - String Validators

'''TO DO FIX'''

def main():
    s = input()
    
    s1 = len(s)
    
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    for i in range(s1):
        if s[i].isalnum():
            count += 1
            
            
    for i in range(s1):
        if s[i].isalpha():
            count1 += 1
            
    for i in range(s1):
        if s[i].isdigit():
            count2 += 1
            
    for i in range(s1):
        if s[i].islower():
            count3 +=1
            
    for i in range(s1):
        if s[i].isupper():
            count4 += 1
        
        
    if count > 0:
        print (True)

    if count1 > 0:
        print (True)
        
    if count2 > 0:
        print (True)
        
    if count3 > 0:
        print (True)
        
    if count4 > 0:
        print (True)

if __name__ == "__main__":
    main()
