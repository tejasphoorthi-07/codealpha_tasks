import random
words=["apple", "orange", "lenovo", "mouse", "pen", "airpods"]
word=random.choice(words)
display=[]
for l in word:
    display.append("_")
guessed_letters=[]
wrong=0
max_wrong=5
print("Welcome to hangman game!!")
print("Guess the word letter by letter")
print("You have ", max_wrong, " wrong attempts\n")
while wrong<max_wrong and "_" in display:
    print("word: "," ".join(display))
    print("Gussed letters : ", guessed_letters)
    guess=input("Enter a letter : ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter ")
    else:
        guessed_letters.append(guess)
    if guess in word:
        print("Correct guess keep going\n")
        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
    else:
        wrong+=1
        print("Its a wrong guess\n")
        print("You have ", max_wrong-wrong," attempts more try!!\n")
if "_" not in display:
    print("You guessed the word", word)
else:
    print("Game Over!!")
