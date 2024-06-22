print("Welcome to the Online Quiz")
playing=input("Do you want to play? ").lower()

if playing != "yes":
    quit()
else:    
    print("ok!! Lets play :)")
    print('''ROUND-1\nABBREVIATION''')

    score=0

    ans = input("what does CPU stands for? ").lower()
    if ans == "control processing unit":
        print("Correct Answer!!")
        score+=1
    else:
        print("Incorrect Answer!!")


    ans = input("what does HTML stands for? ").lower()
    if ans == "hypertext markup language":
        print("Correct Answer!!")
        score+=1
    else:
        print("Incorrect Answer!!")

    ans = input("what does RAM stands for? ").lower()
    if ans == "random access memory":
        print("Correct Answer!!")
        score+=1
    else:
        print("Incorrect Answer!!")

    ans = input("what does ROM stands for? ").lower()
    if ans == "read only memory":
        print("Correct Answer!!")
        score+=1
    else:
        print("Incorrect Answer!!")

    ans = input("what does SQL  stands for? ").lower()
    if ans == "structured query language":
        print("Correct Answer!!")
        score+=1
    else:
        print("Incorrect Answer!!")

    print("ROUND 1 COMPLETED!!")    
    print("You got " + str(score) + " questions correct")
    print("you got " +str((score/5)*100) + "%")
