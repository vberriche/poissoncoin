from PIL import Image as im
from PIL import *
from random import randint as al
from random import shuffle as shf
from PIL import ImageDraw
from PIL import ImageFont

base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

coord = []

for y in range(0,241,120):
	for x in range(0,241,120):
		coord+=[[x,y]]

pieces = {}
for k in range(0,9):
	pieces['p'+str(k)] = im.open(str(k)+".png")
#	pieces['p'+str(k)] = im.open("0.png")

police = ImageFont.truetype("DejaVuSans-Bold.ttf", 30)
ABC = ['A','B','C','D','E','F','G','H','I']

for n in range(0,21):		# nombre de puzzle
	puzzle = im.new('RGB',[360,360],color='white')
	ordre = [ k for k in range(0,9) ]
	nom = ''
	shf(ordre)

	texteABC = ImageDraw.Draw(puzzle)

	# Génération du puzzle
	for k in range(0,9):
		if(1==1):	# choose between random translation
			xk=coord[k][0]+al(0,40)
			yk=coord[k][1]+al(0,40)
			puzzle.paste(pieces['p'+str(ordre[k])],[xk,yk])
			texteABC.text((xk+20,yk+20),ABC[k],(0,0,0),font=police)


	# Génération du nom
	for k in range(0,12):
		nom+=base58[al(0,57)]

	# I let you programm something to save filenames

	# Enregistrer l'image
	puzzle.save("images/puzzle-"+nom+".png")
