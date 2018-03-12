#- coding:utf-8

from math import log as log
from random import *
import time
from ipdb import set_trace as st

base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
email = "0123456789abcdefghijklmnopqrstuvwxyz.-_@#"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def bd(chaine):			# convert a base58 number into a decimal number
	chaine=str(chaine)
	s = 0
	try:
		for k in range(0,len(chaine)):
			n = len(chaine)-k-1
			s += base58.index(chaine[k])*(58**n)
		return s
	except:
		return 0
	
def db(nombre):			# convert a decimal number into a base58 number
	l = int(log(nombre)/log(58))
	chaine = ""
	for m in range(l,-1,-1):
		k = int(nombre/58**m)
		nombre -= k*58**m
		chaine += base58[k]
	return chaine
	
def verify_fool_password(passd):  # verify that password only contains lowercase characters
	try: 
		for i in range(0,len(passd)):
			a = lowercase.index(passd[i])
		return True
	except:
		return False

def error_code(key):
		s = 0
		for c in key:
			s += base58.index(c)
		return (s%58)

def hash_passd(passd):			# return a funny base58 hash of the fool password (3 characters)
	try:
		hash_dec = lowercase.index(passd[0])*271+lowercase.index(passd[1])*269+lowercase.index(passd[2])*263+lowercase.index(passd[3])*257
		for k in range(4,len(passd)):
			hash_dec += lowercase.index(passd[k])
		hash58 = db(hash_dec)
	except:
		hash58 = "111"

	if(len(hash58)==1):
		hash58 = "11"+hash58
	if(len(hash58)==2):
		hash58 = "1"+hash58
	if(len(hash58)>3):	# should not happen
		hash58 = hash58[:3]   

	return hash58
	
def private_key_generator(epoch,what,infos):
# 1 info
# 6 characters epoch
# 24 available
# 1 for seed
# 1 for error code

	try:
		chain = ''
		date = db(int(epoch)) # 6 characters for timestamp
		if(what==1):					# if no password is set (not implemented yet)
			# 23 random letters :
			for k in range(0,24):
				chain += choice(base58)
		if(what==2):				# if a fool password is set
			chain+= hash_passd(infos)  # add a 3 characters hash
			for k in range(0,22):		# and 21 random characters
				chain += choice(base58)
			
		plain_private_key = str(what)+date+chain

		pk = ''

		# adding a one-digit seed
		seed = randrange(0,58)
		for c in plain_private_key:						
			pk += base58[(base58.index(c)+seed)%58]
		pk += base58[seed]

		# One digit error code
		s = error_code(pk)
		pk += base58[s]

		return pk
		
	except:
		"Error !"

def rot29(key):		# This will be the new standard of cryptography for cryptocurrencies!
	key = key[:-1] # remove error code
	key = key.replace('SecretPoisson-','')
	key = key.replace('PublicPoisson-','')

	new_key = ''	
	for c in key:						
		new_key += base58[(base58.index(c)+29)%58]
	
	s = error_code(new_key)
	new_key += base58[s]
	
	return new_key

print("Please, give a stupid password (4-12 lowercase letters like your pet's name)")

foolpassd = input("My password is : ")

while(verify_fool_password(foolpassd) is not True and len(foolpassd)<4):
	print('Only lowercase letters. For example \"IloveU" does not work because there are uppercase letters')
	foolpassd = input("My password is : ")
	
print("\nKeys generator processing... Please wait...")
time.sleep(10)
new_private_key = "SecretPoisson-"+private_key_generator(time.time(),2,foolpassd)
print(new_private_key)
time.sleep(3)
new_public_key = "PublicPoisson-"+rot29(new_private_key)
print(new_public_key)
