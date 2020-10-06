import csv
import random

global secretstring
word_file=open("RandomWordsProject1.txt",'r')
i=0
x=random.randrange(0,9)
for line in word_file:
	if(i==x):
		secretstring=line
	i+=1
c=len(secretstring)
good=" _________     \n|         |    \n|              \n|              \n|              \n|              \n|              \n"
head=" _________     \n|         |    \n|         0    \n|              \n|              \n|              \n|              \n"
body=" _________     \n|         |    \n|         0    \n|         |    \n|              \n|              \n|              \n"
larm=" _________     \n|         |    \n|         0    \n|        /|    \n|              \n|              \n|              \n"
rarm=" _________     \n|         |    \n|         0    \n|        /|\\  \n|              \n|              \n|              \n"
lleg=" _________     \n|         |    \n|         0    \n|        /|\\  \n|        /     \n|              \n|              \n"
dead=" _________     \n|         |    \n|         0    \n|        /|\\  \n|        / \\  \n|              \n|              \n"

wordbank=""
guesses=""
var=True
state=good
u=0
guess=" "

def yeet():
	r=""
	for char in secretstring:
		if char in guesses:
			r+=char
		else:
			r+="_"
	if(r==secretstring):
		var=False
		print("you won")
	print(r)
print("Your word has ",c," characters")
while var:
	
	print(wordbank)
	guess=input("Please enter a guess:\n")
	guesses+=guess
	if(guess not in secretstring):
		wordbank+=guess+", "
		u+=1
		if(u==1):
			state=head
			
		if(u==2):
			state=body
			
		if(u==3):
			state=larm
			
		if(u==4):
			state=rarm
			
		if(u==5):
			state=lleg
			
		if(u==6):
			state=dead
			print(state)
			print("you lost")
			print("your word was: ", secretstring)
			break;
	
	print(state)
	yeet()
	