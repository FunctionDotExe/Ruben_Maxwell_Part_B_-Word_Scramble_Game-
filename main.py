#importing the library "random"
import random
Lives = 5

#Words being used
WORDS = ('earth','people','code','graduation','gaming','family','quarrantine','sick','Home',
'level','up','run','cat','dog','magic','zork','python','java','html','happy','sad','end','player','why','just','no','electronic','mechatronics','humans','life','counter','words','science','subject')

#Variables
word = random.choice(WORDS) 
correctword= word
scrambler = ''
guess = ''

# Start of what is being outputed to the person playing
print("Welcome to Word Scramble!")
print("In This game u need to unscramble the word!")

while word:
    position = random.randrange(len(word))
    scrambler += word[position]
    word = word[:position] + word[(position + 1):] 

print('The Word was:', scrambler)
guess = input('Your Guess: ')

#if not correct word
while guess != correctword:
    print("Try Again")
    Lives = Lives - 1
    print("You have {} Lives Left ".format (Lives))
    guess = input('Your Guess: ')
    #lost all lives
    if Lives <= 0 :
      print("well, Im sorry, you lost :(")
      print("The Word was {}".format (correctword))
      #kicks em out of the game :P
      exit()
 
#if they got the word correct
if guess == correctword:
    print("NICE, you got the answer correct!:D")

