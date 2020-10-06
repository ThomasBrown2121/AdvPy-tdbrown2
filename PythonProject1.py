import random
import time
import math

# stages of potential outcomes in hangman:
hangman_visual = [
   '''
    _ _ _
  |     |
  |   
  |  
  |
  |
  |
  |
 _|_______
   ''',
   '''
   _ _ _
  |     |
  |     O
  |  
  |
  |
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |     |
  |
  |
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |   \ |
  |
  |
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |   \ | /
  |
  |
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |   \ | /
  |     |
  |
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |   \ | /
  |     |
  |    ( 
  |
  |
 _|_______
    ''',
    '''
   _ _ _
  |     |
  |     O
  |   \ | /
  |     |
  |    ( )
  |
  |
 _|_______
    '''
]


# read in data function here
def readfcn():
   A = open("RandomWordsProject1.txt", 'r')
   listholder = []
   for word in A:
      listholder.append(word.strip())
   A.close()
   return listholder
   
# random number generator
def randomnum(Words):
   x = random.randrange(0,len(Words))
   return x

# Outputs the amount of blank spaces, coresponding to the length of the word.
def equivalenceLen(Word):
   s = '_'*len(Word)
   return s

def replacer(Word,hypenSpace,guessed_letter):
   for index in range(len(Word)):
      if Word[index] == guessed_letter:
         hypenSpace.replace(hypenSpace[index],guessed_letter)
      return hypenSpace

#################################################################################################
Chances = 0

# Beginning of users input! 
userInput = input("User please enter your name:")
print(userInput)
# Words is storing the function of readfcn()
Words = readfcn()
#print(Words)

RandomNumholder = randomnum(Words)
Word = Words[RandomNumholder]
hypenSpace = equivalenceLen(Word)

found = False

while Chances < 6 and hypenSpace is not Word:
   print(hangman_visual[Chances])
   print(hypenSpace)
   print(" ")
   guessed_letter = input("Enter a letter: ")
   for character in Word: 
      if character == guessed_letter:
         found = True

   if found == True:
      print("You guessed correctly.")
      print(hangman_visual[Chances])
      hypenSpace = replacer(Word,hypenSpace,guessed_letter)
   else:
      print("You guessed incorrectly.")
      Chances = Chances + 1
      print(hangman_visual[Chances])
   
   found = False

if Tries == 0:
   print("YOU HAVE LOST!")

else:
   print("YOU HAVE WON!")
   


