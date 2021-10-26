from random import random

p_w3 = 0.268
win_1 = []
win_2 = []
win_3 = []

def game(p_w3):
    winner = None
    p_w2 = random()
    p_w1 = random()
    print("p_w2 is" + str(p_w2))
    print("p_w1 is" + str(p_w1))
    while winner == None:
        result3 = lift(p_w3)
        result2 = lift(p_w2)
        result1 = lift(p_w1)
        if result1 == True and result2 == True and result3 == True:
            if min(p_w1,p_w2,p_w3) == p_w1:
                print("The winner is robot 1")
                winner = 1
                win_1.append(1)

            elif min(p_w1,p_w2,p_w3) == p_w2:
                print("The winner is robot 2")
                winner = 1
                win_2.append(1)

            else:
                print("The winner is robot 3")
                winner = 1
                win_3.append(1)

        elif result1 == True and result2 == True:
            if min(p_w1,p_w2) == p_w1:
                print("The winner is robot 1")
                winner = 1
                win_1.append(1)

            elif min(p_w1,p_w2) == p_w2:
                print("The winner is robot 2")
                winner = 1
                win_2.append(1)

        elif result1 == True and result3 == True:
            if min(p_w1,p_w3) == p_w1:
                print("The winner is robot 1")
                winner = 1
                win_1.append(1)

            elif min(p_w1,p_w3) == p_w3:
                print("The winner is robot 3")
                winner = 1
                win_3.append(1)

        elif result2 == True and result3 == True:
            if min(p_w2,p_w3) == p_w1:
                print("The winner is robot 2")
                winner = 1
                win_2.append(1)

            elif min(p_w2,p_w3) == p_w3:
                print("The winner is robot 3")
                winner = 1
                win_3.append(1)

        elif result1 == True:
            print("The winner is robot 1")
            winner = 1
            win_1.append(1)

        elif result2 == True:
            print("The winner is robot 2")
            winner = 1
            win_2.append(1)
        elif result3 == True:
            print("The winner is robot 3")
            winner = 1
            win_3.append(1)



def lift(p_w):
    performance = random()
    if performance > p_w:
        return False
    else:
        return True

n = 100
num2win = 0
for i in range (n):
    game(p_w3)
print("The number of times robot 1 wins is" + str(sum(win_1)))
print("The number of times robot 2 wins is" + str(sum(win_2)))
print("The number of times robot 3 wins is" + str(sum(win_3)))
