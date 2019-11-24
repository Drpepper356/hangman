import random
words = ["lion", "eagle", "bear", "whale", "dolphin", "salmon","sparrow","falcon"]
random_word = random.choice(words)
length_of_word = (len(random_word))
answer = []
count = 0
used_words = []


for character in random_word:
    answer.append("-")

name = input("Lets play some hangman!\nEnter your name :")
print("Ok", name, "your word has", length_of_word, "letters\nThe theme is animals")
print(answer)
player_guess = input("Enter a letter :")

while count < 6:


    if player_guess in used_words:
        print("You've already used that letter!")
    if len(player_guess) > 1:
        print("You can only input one letter at a time!")
    else:
        used_words.append(player_guess)
        if player_guess in random_word:
            print("Correct!")
            used_words.append(player_guess)
        else:
            print("That's incorrect")
            count += 1
            used_words.append(player_guess)
        if count == 1:
            print("You have 5 guesses left")
        if count == 2:
            print("You have 4 guesses left")
        if count == 3:
            print("You have 3 guesses left")
        if count == 4:
            print("You have 2 guesses left")
        if count == 5:
            print("This is your last guess!")


    for n, character in enumerate(random_word):
        if character == player_guess:
            answer[n] = character
    print(answer)
    if not '-' in answer:
        print("You won! Good job")
    if count == 6:
        print("Game Over!", "The word was", random_word)

    player_guess = input("Enter a letter :")






