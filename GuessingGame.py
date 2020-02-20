

print("Hello, you're about to play a Guessing game.")
print("I'll give you a hint and you have to guess the word.")
print("But, the trick is you have a limit of 3 guesses.")
print("ALL THE BEST AND ENJOY!!")

secret_word = "money"
print("\nHINT: Root of all evil.")

guessed_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while (guessed_word != secret_word and not(out_of_guesses)):
    if (guess_count < guess_limit):
        if (guess_count == 0):
            user_input = input("Guess the word: ")
            guessed_word = user_input.lower()

        elif (guess_count == 1):
            user_input = input("Second chance, guess the word: ")
            guessed_word = user_input.lower()

        else:
            user_input = input("LAST CHANCE, guess the word: ")
            guessed_word = user_input.lower()
        guess_count += 1

    else:
        out_of_guesses = True

if (out_of_guesses):
    print("Out of Guesses, YOU LOSE! THE CORRECT WORD IS: "+secret_word)

else:
    print("CONGRATULATIONS!!! YOU WIN!!!")
