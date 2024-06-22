import random
Range=input("enter a number: ")
if Range.isdigit():
    Range= int(Range)
    if Range<=0:
        print("Please type a Number above 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
random=random.randint(0,Range)
guesses=0

while True:
    guesses+=1
    user_guess=int(input("Make a guess: "))
    #if user_guess.isdigit():
    #  user_guess=int(user_guess)
    #else
    #  print("please type a number next time")
    #  continue
    if user_guess==random:
        print("You got it Right!!")
        break
    elif user_guess>random:
        def hint1():
            print("you got it wrong!!")
            a=input("Do you want a hint? ").lower()
            if a =="yes":
                print("You were above the number!")
            else:
                print("super keep going!!")
        hint1()        
    elif user_guess<random:
        def hint2():
            print("you got it wrong!!")
            a=input("Do you want a hint? ").lower()
            if a =="yes":
                print("You were below the number!")
            else:
                print("super keep going!!")
        hint2()        
                
    else:
        print()
        #print("You were below the number!")
print("you got it in",guesses,"guesses")