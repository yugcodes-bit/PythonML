import random

word_list = ['baboona', 'camel', 'giraffe']
chosen_word = random.choice(word_list)

print(chosen_word)

placeholder =""
for i in range(len(chosen_word)):
    placeholder += "_"
print (placeholder)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("Already guessed the letter")
    display =""
    
    for a in chosen_word:
        if(a == guess):
            display += a
            correct_letters.append(guess)    
        elif a in correct_letters:
            display += a     #if 
        else:
            display += "_"

    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} ,its not in the word")
        if lives == 0:
            game_over = True
            print("You lose")        

    if "_" not in display:
        game_over=True
        print("You win")
    print(display)     
    print(lives)


   

