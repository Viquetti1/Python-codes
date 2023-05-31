import random as rd

word_list = ["ardvark", "baboon", "camel","florianopolis","paralelepipedo"]
chosen_word = rd.choice(word_list)
print(chosen_word)
chosen_word_in_list = []
#for to put the random word in a list


for i in chosen_word:
    chosen_word_in_list += i.split()


display = []

word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"

life = 5
win = 0


while win == 0:   
    print(display)
    print(chosen_word_in_list)
    guess = input("Guess a letter! ").lower()
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        if display == chosen_word_in_list:
            win = 1
            break
    if guess != letter:
            life -= life 
            print(f"The letter {guess} isn't in the word, try again another letter, you still have {life} chances ")
        

print(f"You win!! the word is {chosen_word}")
print(life)











       










