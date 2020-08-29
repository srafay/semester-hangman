from random import randint  # to generate the random words out of list

word_array = ['bye', 'hello', 'prestegious', 'weather']  # list of words for player
number_of_words = len(word_array)
random_word = word_array[randint(0, number_of_words - 1)]
word_length = len(random_word)
# these set of conditions define how the words will be replaced by blanks inorder for user to guess them
# here variable loop_iteration is used which will limit the iteration of the loop according to its length
if (word_length > 1 and word_length <= 3):
    loop_iteration = word_length - 1
elif (word_length > 3 and word_length <= 5):
    loop_iteration = word_length - 2
elif (word_length > 5 and word_length <= 8):
    loop_iteration = word_length - 3
elif (word_length > 8 and word_length <= 10):
    loop_iteration = word_length - 6
elif (word_length > 10 and word_length <= 13):
    loop_iteration = word_length - 8
else:
    loop_iteration = word_length - 4
answers = []
guess_word = []
for x in random_word:  # breaking the word into letters and saving them into array to have more control over them
    guess_word.append(x)

word_pos_dict = {}

for x in range(0, loop_iteration):  # looping over a word to skip letters for user to guess them
    placer = randint(0, word_length - 1)
    if (guess_word[placer] == '_'):
        continue
    word_pos_dict.update({placer: guess_word[
        placer]})  # dictionary is used here to remember the position of the letter from which it was removed so later it can be placed at the same position when its guessed correctly
    answers.append(
        guess_word[placer])  # letter replaced will be saved in dictionary and array along with their position
    guess_word[placer] = '_'
final_word = ''


def word_maker(pos, alph):  # function for returning updated word after user guess the letter correctly
    any_word = ''
    guess_word[pos] = alph
    for x in guess_word:
        any_word += x
    return any_word, guess_word


for x in guess_word:  # loop to represent the word in user-friendly way instead of an array
    final_word += x

player_life = 3  # player life initiated

if __name__ == "__main__":
    while player_life != 0:  # main loop of the game will run untill player life reaches zero
        print(
            "The word you have to guess is : " + final_word + '\n')  # presenting the user with word they have to guess
        p_in = input("Enter the guessed letter : ")  # taking letter inpur from user
        if p_in in word_pos_dict.values():  # checking if user has guessed the word correclty
            print("You guessed correct")
            # hfor key, value in list(word_pos_dict):  # replacement of the guessed word
            for key, value in word_pos_dict.items():  # replacement of the guessed word
                if value == p_in:
                    final_word, guess_word = word_maker(key, value)  # calling of fuction to display updated word
                    # word_pos_dict.pop(key)  # removing the letter entry from dictionary which has been guessed correctly

        else:  # deduction of player life and displaying incase of wrong answer
            player_life -= 1
            print("\nyou guessed wrong and your life will be deducted, current life : " + str(player_life))
        if '_' not in guess_word:  # game ending condition if theres no spaces left to guess game will end
            print("\nYou have guessed all the alphabets correctly grats : " + final_word)
            break
        if (
                player_life == 0):  # condition to show specific  message when player life reached to zero instead of abruptly ending the loop
            print("You have wasted all your lifes try again later")
            break
