name = input("Type your name: " )
print("Welcome" , name, "to ths adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go ?(left/right) " ).lower()

if answer == "left":
    answer = input(" You came to a river, you can walk around it or swim across ? (walk/cross)")

    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")

    elif answer == "walk":
        print("You walked for many miles and ran out of water and you lost the game. ")

    else:
        print("Not a valid option. You lose.")
        
if answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you what to cross it or head back(cross/back)? (cross/back) ")

    if answer == "back":
        print("You go back and are ran over by a truck and lose")

    elif answer == "cross":
        anwser = input("You cross the brdge and meet a stranger. Do you talk to the stranger(yes/no)? ")
        
    else:
        print("Not a valid option. You lose.")
        
if answer == "yes":
   answer == input("You spoke to the stranger and they give you gold. You WIN! ")
            
elif answer == "no":
    print("You ignored the stranger and they are offended. You LOSE! ")
        
else:
        print("Not a valid option. You lose.")
            
           
print("Thank you for trying", name) 
 
