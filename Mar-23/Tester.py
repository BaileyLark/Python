import random

questions = [["8 x 7", "56"], ["12 x 9", "108"], ["9 x 6", "54"], ["9 x 4", "36"], ["12 x 7", "84"], ["8 x 6", "48"], ["9 x 8", "72"]]

exit = True

while(True):
    
    randval = random.randint(0, 6) # answer 

    answer = input(f"{questions[randval][0]}: ")

    if answer == questions[randval][1]:
        print(f"Correct\n") 
    else: 
        print("Wrong\n")





