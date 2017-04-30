#Author: Jennifer Cafiero
#Date: April 28, 2017
#HackerRank Python - Lists

if __name__ == '__main__':
    N = int(input())
    cmds = []
    i = 0
    e = 0
    for x in range(N):
        command = input()
        command = command.split()
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            cmds.insert(i,e)
        elif command[0] == "print":
            print(cmds)
        elif command[0] == "remove":
            e = int(command[1])
            cmds.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            cmds.append(e)
        elif command[0] == "sort":
            cmds.sort()
        elif command[0] == "pop":
            cmds.pop()
        elif command[0] == "reverse":
            cmds.reverse()
        else:
            print('Command not found, skipping command')
            
        
