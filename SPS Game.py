import random
    

lst= ['stone','paper','scissors']
i=0
while i<4:
    print("Enter one of the option :- \n1.STONE\n2.PAPER\n3.SCISSORS")
    ans=int(input())
    current=random.choice(lst)
    print('PC choice : ',current)

    if current == 'stone' and ans== 1:
        print("Draw")
    elif current == 'stone' and ans==2:
        print("You Won!!!")
    elif current == 'stone' and ans == 3:
        print("You Lose")
    elif current == 'paper' and ans == 1:
        print("You Lose")
    elif current == 'paper' and ans == 2:
        print("Draw")
    elif current == 'paper' and ans == 3:
        print("You Won!!!")
    elif current == 'scissors' and ans == 1:
        print("You WON!!!")
    elif current == 'scissors' and ans == 2:
        print("You Lose")
    elif current == 'scissors' and ans == 3:
        print("DRAW")
    else:
        print("invalid option,please try again")


