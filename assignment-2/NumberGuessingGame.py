import random
systemGuess=random.randint(1,100)
count=0
while count<7:
    UserGuess=int(input("Guess Number :"))
    count+=1
    if UserGuess==systemGuess:
        print("congratulations you guess the number, attempts:",count)
        break
    else:
        if(UserGuess<systemGuess):
            print(f"Guess a Greater Number, Attempts left : {7-count}")
        else:
            print(f"Guess a Smaller Number, Attempts left : {7-count}")            
    if count==7:
        print("correct number is:",systemGuess)
        print("Guess Failed try again")

