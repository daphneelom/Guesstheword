# GuessTheWord Game
# The word game where players try to find out a random word by guessing the characters one by one
# It takes the level of the game as user input and start the game
# User can retry if they after failed to find the word


from words import get_word


def print_log(text):
    # Function print log helps to print the log in both console and output file
    f.writelines(text)
    print(text)


def play(play_level):
    # Main function which has game play core script

    # Call the external function to get the word based on the level
    word = get_word(play_level)
    word_length = len(word)

    # Set the extra guess to 5, so user can get 5 more guesses extra
    extra_guess = 5
    total_guesses = word_length + extra_guess

    print_log("Starting the Game...")
    print_log("The Word you need to guess has '{}' characters".format(word_length))

    # Initialize the list with _ so we can display to the user with masked values
    guess_word = ['_'] * word_length
    guessed = False

    while not guessed:
        # till user able to guess or guesses over loop will continue else break
        print_log("\n\nGuesses left: {}".format(total_guesses))
        print_log('\n\nword: {}'.format('  '.join(guess_word)))
        print_log("\n\n")
        print_log("Enter a Letter:  ")
        char_input = input()
        found = False

        for idx, letter in enumerate(word):
            # loop through all the words and find the user input is a match word or not
            if char_input == letter and guess_word[idx] == '_':
                guess_word[idx] = letter
                print_log("Good Guess !!")
                found = True
                # if the word match, then set found = true and set the character in masked list and break the loop
                break

        if not found:
            print_log("Not in the word, Try Again !!")

        # decrease the guess each time
        total_guesses = total_guesses - 1

        # if the final word is matched with the guessed word, then end the program
        if word == ''.join(guess_word):
            guessed = True
        elif total_guesses < 1:
            break

    if guessed:
        # provide the skill map to the user based on the remaining guess left
        print_log("\n\nCongratulations you win, Word is : {}\n\n".format(word))
        skill_map = {5: "Marvellous", 4: "Excellent", 3: "Very good", 2: "Nice", 1: "Good", 0: "Ok"}
        print_log("Your Guess level is: '{}'".format(skill_map[total_guesses]))

    else:
        # If user not able to find the word and still they want to retry get the input and proceed further
        print_log("\n\nYou lost... Want to try again press 'y'")
        retry = input()
        if retry == 'y':
            game_level = choose_level()
            play(game_level)
        else:
            # if not want to continue end the game and return
            return


def choose_level():
    # Get the user input and return the user game level
    print_log("Enter the game difficulty level\n"
              "1. Easy\n"
              "2. Medium\n"
              "3. Difficult\n\n")
    game_level = input("Enter 1 or 2 or 3:  ")
    if game_level not in ['1', '2', '3']:
        # if it is not a valid input, then end the game and ask to restart
        print_log("Invalid choice, Play Again")
        exit()
    else:
        game_level = int(game_level)

        level_map = {
            1: "Easy",
            2: "Medium",
            3: "Difficult"
        }
        print_log("Level {} selected".format(level_map[game_level]))
        # return the game level for further processing
        return game_level


if __name__ == '__main__':
    # game flow start from here
    # open the game_log file to store all the logs
    f = open('game_log.txt', 'w+')

    print_log("Welcome to GuessTheWorld")
    # choose the game level
    level = choose_level()

    # call the main play function with the level
    play(level)
    print_log("\n\nThanks for playing ....")

    # close the file
    f.close()

    # process ends here
