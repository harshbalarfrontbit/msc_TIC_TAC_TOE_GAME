import random

pos = ["-","-","-","-","-","-","-","-","-"]
wincase = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
num = ['1','2','3','4','5','6','7','8','9']

def printboard():
    print(" ",pos[0]," | ",pos[1]," | ",pos[2])
    print("-----------------")
    print(" ",pos[3]," | ",pos[4]," | ",pos[5])
    print("-----------------")
    print(" ",pos[6]," | ",pos[7]," | ",pos[8])

def winplayer():
    for i in wincase:
        if pos[i[0]] == pos[i[1]] == pos[i[2]] == "X":
            printboard()
            print("Congratulations! You win!")
            return True
    return False

def wincomp():
    for i in wincase:
        if pos[i[0]] == pos[i[1]] == pos[i[2]] == "O":
            printboard()
            print("Sorry! Computer won!")
            return True
    return False

def playerturn():
    entnum = input("Choose a number between 1 to 9 corresponding to the position you want to put your X: ")
    if entnum not in num:
        print("Enter a valid position between 1 and 9 which is not taken already: \n")
        playerturn()
    else:
        entnum = int(entnum)
        pos[entnum-1] = "X"
        num.remove(str(entnum))
        if num==[]:
            printboard()
            print("It's a Tie !!")
            return
        elif winplayer():
            return
        computerturn()

def computerturn():
    for i in wincase:
        if pos[i[0]] == pos[i[1]] == "O" and pos[i[2]] == "-":
            pos[i[2]] = "O"
            num.remove(str(i[2]+1))
            break
        elif pos[i[1]] == pos[i[2]] == "O" and pos[i[0]] == "-":
            pos[i[0]] = "O"
            num.remove(str(i[0]+1))
            break
        elif pos[i[2]] == pos[i[0]] == "O" and pos[i[1]] == "-":
            pos[i[1]] = "O"
            num.remove(str(i[1]+1))
            break
    else:
        for i in wincase:
            if pos[i[0]] == pos[i[1]] == "X" and pos[i[2]] == "-":
                pos[i[2]] = "O"
                num.remove(str(i[2]+1))
                break
            elif pos[i[1]] == pos[i[2]] == "X" and pos[i[0]] == "-":
                pos[i[0]] = "O"
                num.remove(str(i[0]+1))
                break
            elif pos[i[2]] == pos[i[0]] == "X" and pos[i[1]] == "-":
                 pos[i[1]] = "O"
                 num.remove(str(i[1]+1))
                 break
        else:
            j = random.choice([int(i) for i in num])
            pos[j-1] = "O"
            num.remove(str(j))
    if wincomp():
        return
    printboard()
    playerturn()

print("Let's play a game of Tic Tac Toe\nYou will be 'X' and I will be 'O'")
printboard()
playerturn()
