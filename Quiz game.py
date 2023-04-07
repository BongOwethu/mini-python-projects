
print(" Welcome to my computer quiz!")

playing = input( "Do you want to play? (Yes/No) ")

if  playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Well done!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Good job!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Good job!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Excellent!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does CD stand for? ")
if answer.lower() == "compact disc":
    print("Good job!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does AGP stand for? ")
if answer.lower() == "accelerated graphic support":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does HHD stand for? ")
if answer.lower() == "hard disk drive":
    print("Good job!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does IDE stand for? ")
if answer.lower() == "intergrated device electronics":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Well done!")
    score += 1

else:
    print("Incorrect!")

print("You got " +  str((score / 10 ) *100 )  + "%.")








    
    
