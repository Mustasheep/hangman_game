import random
from Hangman import logo, stages
from listas import listas

print(logo)

lives = 6

chosen_game = random.choice(listas)
chosen_word = random.choice(chosen_game)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

if "manga" in chosen_game:
    game = "uma fruta"
elif "Preto" in chosen_game:
    game = "uma cor"
else:
    game = "um animal"

print(f"\n\nDica: é {game} e contém {len(chosen_word)} letras.\n")

game_over = False
correct_letters = []
incorrect_letters = ""

while not game_over:
    print(f"---------------------------- Você possui {lives} tentativas ----------------------------\n")
    guess = input("Escolha uma letra: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        incorrect_letters += guess + " - "

        if lives == 0:
            game_over = True
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Você Perdeu! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A palavra correta era: {str(chosen_word).upper()} ~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\n")
    print(display)

    if "_" not in display:
        game_over = True
        print("\n*********************************** Você Venceu! ************************************")

    print(stages[lives])
    print(f"Letras incorretas: {incorrect_letters}\n")
