import random
'''
1 for Snake
-1 for water 
0 for gun.

now we create a snake water gun game for fun .
'''
computer=random.choice([1, -1, 0])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer==you):
    print("It's a draw")
else:
    if(computer==-1 and you==1 ):
        print("you win")
    elif(computer==-1 and you==0 ):
        print("you Lose")
    
    elif(computer==1 and you==0 ):
        print("you Win")
    
    elif(computer==1 and you==-1 ):
        print("you Lose")

    elif(computer==0 and you==-1 ):
        print("you Win")
    elif(computer==0 and you==1 ):
        print("you Lose")

    else:
        print("Something went wrong!")