# Match case statements are the latest technologies
'''
Switch case statements are used on the version before 3.8 python versions
Match case statements are used in newer versions of python after 3.10
'''
# Taking input from user of yes or no questioning, Do you want to vote or not
# If yes then the program will congratulate you and if not then it will request you to vote for your country's next leader
x = input("Do you want to vote: ")

match x:
    case "Yes":
        print("Awesome! That you want to vote for your country :)")
    case "No":
        print("It's sad to hear that, You should vote for choosing best for your country :(")

    # For default case we use underscore(_) as default or else
    case _ if(x=="Y"): # Here is how we can use if inside a case with using uderscore before the condition
        print("Awesome! That you want to vote for your country :)")
    case _ if(x=="N"): # Same as before for N as no for the input
        print("It's sad to hear that, You should vote for choosing best for your country :(")
    case _:
        print("Input range exceeded")
