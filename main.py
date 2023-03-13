
# importing Random module which will help generate a random integer
import random


# Start of the program, it will print the heading

print("\n\n\n             Welcome to the Number-Guessing Game\n                                          Made by - Naman Nanda\n\n\n")


# using try and except block as we want only integers and giving it a different datatype will pring the exception part
try:
    # Defining a variable called Tries, it will store the number of total tries
    Tries = int(input("Enter the number of tries: "))
    # Defining another variable to keep the value of total tries as tries variable will keep changing
    Orginal_try = Tries
    # Taking input for the Starting and Ending Range
    St_Range,End_Range = map(int,input("Enter the range you want to guess in: ").split(" "))
    # Using randint function from the random module to generate a random integer in the given range and storing it in To_Guess variable
    To_Guess = random.randint(St_Range,End_Range+1)
except Exception as error:
    print("ENTER ONLY INTEGERS")    

# Using while loop to ask for guess again and again until the tries have finished
while Tries>=0:
    # Taking input for the guessed variable
    Guessed_var = int(input("Enter your guess: "))
    # decrementing the value of tries by one every time it goes off
    Tries -=1
    # checking if the user guessed value lies in the previously given range or not
    if End_Range >= Guessed_var >= St_Range:
        # using if-else condition statements to check if the user guessed is equal to the random integer generated
        if To_Guess==Guessed_var and Tries==Orginal_try:
            print("Wohooo !!, You won on the first try. Thats impressive.\n")
            break
        elif To_Guess==Guessed_var:
            print("You won !!, you were able to guess the right number before you ran out of tries, nice!!\n")   
            break 
        elif To_Guess==Guessed_var and Tries==1:
            print("Phewww, you guessed it right at the last try, nice luck!!\n")    
            break
        elif To_Guess!=Guessed_var and Tries==0:
            print(f"oops you lost, have better luck next time!!\nthe right Guess was {To_Guess}")
            break
        else:
            print("Nahh, wrong guess\n")
        if Tries == 2:
            print("Guess Carefully, you have only 2 tries remaining\n")
        elif Tries == 1:
            print("THIS IS YOUR LAST TRY!!\n")
           
    else:
        print("The Number you entered is out of range, Try Again !!")
        

