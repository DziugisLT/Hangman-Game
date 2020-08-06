import random

words = ['event', 'ice', 'square', 'view', 'handle']

randomWord = words[random.randint(0, len(words)-1)]
guessCount = 3
wrongGuess = []

print('Word length: ' + str(len(randomWord)))
print('Guesses left: ' + str(guessCount))
print('Wrong guesses: ' + str(len(wrongGuess)))
wordUnknown = ('-'*(len(randomWord)))
word = list(wordUnknown)
print('Word: ' + "".join(word))

while "-" in "".join(word):
    wordGuess = input("Guess the letter:")
    if wordGuess in randomWord:
        characterPlace = randomWord.find(wordGuess)
        word[characterPlace] = wordGuess
        if str(wrongGuess) != '[]':
            print("Wrong guesses you\'ve made already: " + str(wrongGuess))
        print('Word: ' + "".join(word))
    else:
        guessCount -= 1
        wrongGuess.append(wordGuess)
        if guessCount == 0:
            print("You lost!")
            print("The word was: " + str(randomWord))
            break
        print("This letter is not in the word!")
        print("You are left with " + str(guessCount) + " guesses")
        print("Wrong guesses you\'ve made: " + str(wrongGuess))


if '-' not in "".join(word):
    print("You won!")