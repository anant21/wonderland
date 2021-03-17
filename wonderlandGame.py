# Wonderland Game
# Creator: Anant Gangwar
# Date: March 17, 2021
# Github: anant21
# LinkedIn: anant-gangwar

from sys import exit, argv
import pyfiglet
import os
import time

def secret(name):
	secret = input('Enter the secret: > ')
	if secret == name:
		print("\nWoohoo! Correct.")
	else:
		die("Oops! Your secret was incorrect.", name)

def ufo_room_m(name):
	os.system('clear')
	banner()
	print("\nAll aliens got dispersed after the meeting.")
	print("An alien (Ginny) came by and asked you to marry her.")
	print("What would you do? Marry her, reveal truth, or say nothing.")
	truth = False

	while True:
		choice = input("> ")

		if (choice == "marry her" or choice == "marry") and truth == False:
			print("\nThat was a nice idea. But she hated you for hiding the truth.")
			die("She starved you for 1 week.", name)
		elif (choice == "marry her" or choice == "marry") and truth == True:
			print("\nGood choice! But she's asking your secret to confirm identity.")
			secret(name)

			print("\nGreat! She saved you! She brought you back to the Earth. You both are living happily!")
			print("\nYou Won!")
			exit(0)
		elif (choice == "reveal truth" or choice == "truth" or choice == "tell truth" or choice == "reveal"):
			print("\nShe got influence with your honesty and trustworthiness.")
			print("So, she still wanna marry you. What would you do now?")
			print("Marry her or say nothing?")
			truth = True
		elif choice == "say nothing" or choice == "nothing":
			print("\nYou said nothing. She left!")
			print("You couldn't hide anymore.")
			die("They threw you out of the spaceship.", name)
		else:
			print("\nI got no idea what that means.")


def ufo_room_f(name):
	os.system('clear')
	banner()
	print("\nAll aliens got dispersed after the meeting.")
	print("An alien (Ron) came by and asked you to marry him.")
	print("What would you do? Marry him, reveal truth, or say nothing.")
	truth = False

	while True:
		choice = input("> ")

		if (choice == "marry him" or choice == "marry") and truth == False:
			print("\nThat was a nice idea. But he hated you for hiding the truth.")
			die("He starved you for 1 week.", name)
		elif (choice == "marry him" or choice == "marry") and truth == True:
			print("\nGood choice! But he's asking your secret to confirm identity.")
			secret(name)

			print("\nGreat! He saved you! He brought you back to the Earth. You both are living happily!")
			print("\nYou Won!")
			exit(0)
		elif (choice == "reveal truth" or choice == "truth" or choice == "tell truth" or choice == "reveal"):
			print("\nHe got influence with your honesty and trustworthiness.")
			print("So, He still wanna marry you. What would you do now?")
			print("Marry him or say nothing?")
			truth = True
		elif choice == "say nothing" or choice == "nothing":
			print("\nYou said nothing. He left!")
			print("You couldn't hide anymore.")
			die("They threw you out of the spaceship.", name)
		else:
			print("I got no idea what that means.")


def ufo_room_o(name):
	os.system('clear')
	banner()
	print("\nAll aliens got dispersed after the meeting.")
	print("An alien (Harry) came by and asked you to be his friend.")
	print("What would you do? Accept friendship and reveal truth (ar), accept but not reveal truth (anr), or say nothing(sn).")

	while True:
		choice = input("> ")

		if choice == "anr":
			print("\nThat was a nice idea. But later he hated you for hiding the truth.")
			die("He left you with army.", name)
		elif choice == "ar":
			print("\nGood choice! But he's asking your secret to confirm identity.")
			secret(name)

			print("\nGreat! He saved you! He brought you back to the Earth!")
			print("\nYou Won!")
			exit(0)
		elif choice == "say nothing" or choice == "nothing" or choice == "sn":
			print("\nYou said nothing. He left!")
			print("You couldn't hide anymore.")
			die("They threw you out of the spaceship.", name)
		else:
			print("\nI got no idea what that means.")


def alien(name, gender):
	os.system('clear')
	banner()
	print("\nYou're teleported to Alien spaceship!")
	print("Now you're in the empty room of the spaceship.")
	print("There's nobody around. Aliens are in other room.")
	print("You see a spacesuit hanging and an Emergency exit door.")
	print("\nWhat would you do?")
	spacesuit = False

	while True:
		choice = input("> ")

		if choice == "wear spacesuit" or choice == "wear" or choice == "wear it" or choice == "take spacesuit":
			print("\nNow that you've worn spacesuit. You can join other aliens or take exit from Emergency door.")
			spacesuit = True
		elif (choice == "open door" or choice == "exit" or choice == "jump out" or choice == "take exit") and spacesuit == False:
			die("Oops! There's no oxygen outside.", name)
		elif (choice == "open door" or choice == "exit" or choice == "jump out" or choice == "take exit") and spacesuit == True:
			die("You float around in the space without. You dont get any help for days.", name)
		elif (choice == "join" or choice == "join aliens" or choice == "join them") and spacesuit == False:
			die("You're not their master. You must hide your identity.", name)
		elif (choice == "join" or choice == "join aliens" or choice == "join them") and spacesuit == True:
			print("\nGreat! You've joined them. You're safe now.")

			if gender == "m":
				ufo_room_m(name)
			elif gender == "f":
				ufo_room_f(name)
			elif gender == "o":
				ufo_room_o(name)
			else:
				print("\nUnexpected Gender error!")

		else:
			print("I got no idea what that means.")

def button(name, gender):
	os.system('clear')
	banner()
	print("\nInteresting! You are teleported to the Secret Chamber of Room2.")
	print("You see a locked door.")
	choice = input("> ")

	if choice == "open it" or choice == "unlock it" or choice == "open" or choice == "unlock" or choice == "open door" or choice == "unlock door":
		if key == True:
			print("\nSmart! You got the key. Door is opened.")
			print("Enter inside or Give up?")
			ch = input("> ")

			if ch == "enter inside" or "enter":
				alien(name, gender)
			elif ch == "give up" or ch == "exit":
				print("\nIf you give up, you lose!")
			else:
				print("\nI got no idea what that means.")
		else:
			print("\nGo! Find the Key.")
	else:
		die("You gotta find a way. There's no food/water inside.", name)

def note(name, gender):
	os.system('clear')
	banner()
	print("\nYou find a note inside.")
	choice = input("> ")
	if choice == "read note" or choice == "read it" or choice == "read":
		print("\nNote: Press the red button behind the book.")
		ch = input("> ")

		if ch == "press" or ch == "press button" or ch == "press it":
			button(name, gender)
		else:
			print("\nYou were teleported to the hell for not following instructions. You lose!")
			exit(0)
	else:
		die("You were punished badly for taking the book.", name)

def bookshelf(name, gender):
	os.system('clear')
	banner()
	print("\nWow! There are many books. You see an ancient chinese book.")
	print("Wanna take it or look around?")
	choice = input("> ")

	if choice == "take it" or choice == "take book" or choice == "take":
		note(name, gender)
	elif choice == "look around" or choice == "look":
		print("\nThere's nothing around. You may wanna try other room.")
	else:
		print("\nI got no idea what that means.")

def room1(name, gender):
	os.system('clear')
	banner()
	print("\nYou see a bookshelf and a tomb.\nYou may open the tomb or check bookshelf or look around.")
	choice = input("> ")

	if choice == "check tomb" or choice == "open tomb" or choice == "tomb":
		die("Dangerous Mummy holds your neck tightly.", name)
	elif choice == "check bookshelf" or choice == "bookshelf" or choice == "see bookshelf":
		bookshelf(name, gender)
	elif choice == "look around" or choice == "look":
		print("\nThere's nothing around. You may wanna try other room.")
	else:
		print("\nI got no idea what that means.")


def room2(name):
	os.system('clear')
	banner()
	print("\nRoom 2 is Mysterious Room. ")
	print("You see a lot of money. Also a secret chamber in this room.")
	print("But you can't find it. What would you do?")
	print("Take money? or Find chamber?")
	choice = input("> ")

	if choice == "take money" or choice == "money":
		print("You're so greedy! Told ya its a Mysterious room.")
		die("The castle got destroyed!", name)
	elif choice == "find chamber" or choice == "chamber":
		print("Hah! You can't find anything. Its mysteriously hidden.")
	else:
		print("Re-read above text. Answer again!")


def key(name, gender):
	choice = input("> ")
	global key
	key = False

	if choice == "take key" or choice == "grab key" or choice == "key":
		key = True
		print("\nOkay! You got the key. What next?")
	else:
		die("The bear wakes up and eats your leg.", name)

def tunnel(name, gender):
	print("\nYou see a door.")
	choice = input("> ")

	if choice == "open door" or choice == "open it" or choice == "open":
		print("\nThere is a sleeping bear.\nAlso you see a key lying there.")
		print("What would you do?")
		key(name, gender)
	else:
		print("\nYou gotta do something! You can't stay in the tunnel for long.")


def castle(name, gender):
	os.system('clear')
	banner()
	print("\nThe Castle is extremely beautiful from inside.\nThere are 2 rooms and a tunnel.")

	while True:
		print("\nYou are in the Hall of Castle.")
		print("\nWhat you wanna do? (enter room1, enter room2 or enter tunnel)")
		choice = input("> ")


		if choice == "enter room1" or choice == "room1":
			room1(name, gender)
		elif choice == "enter room2" or choice == "room2":
			room2(name)
		elif choice == "tunnel" or choice == "enter tunnel":
			tunnel(name, gender)
		else:
			print("\nI got no idea what that means.")

def roam(name, gender):
	os.system('clear')
	banner()
	print("\nYou are roaming around. A wizard came by and asks your help.")
	print("Will you help him or not?")
	choice = input("> ")

	if choice == "help" or choice == "yes" or choice == "help him":
		print("Wizard is happy with your help! He helps you in this game.")
		print("You're being teleported to the Hall of the Castle.")
		time.sleep(3)
		castle(name, gender)
	else:
		die("Oops! He was Voldemort. Avada Kedavra.", name)

def die(why, name):
	print("\n$$", why, f" Obviously, you're dead {name}!!")
	exit(0)

def welcome(name, gender):
	os.system('clear')
	banner()

	print(f"\n  WELCOME TO WONDERLAND, {name}")
	print("================================")
	print("\nYou're in a wonderland. There's nothing around you but a castle. \nYour little secret that is your name can help you ;)")
	print("Would you like to enter or roam around? \n\n#(Answer in one word or two.)##\n")

	choice = input("> ")

	if choice == "enter" or choice == "enter castle":
		castle(name, gender)
	elif choice == "roam" or choice == "roam around":
		roam(name, gender)
	else:
		die("You stumble around until you starve.", name)


def start():
	os.system('clear')
	banner()
	print("**Format: python3 wonderlandGame.py <your-name> <gender(m/f)>\n")
	print(">> python3 wonderlandGame.py Alice f")
	print(">> python3 wonderlandGame.py Bob m\n")

	script, name, gender = argv

	if gender == "m" or gender == "f" or gender == "o":
		welcome(name, gender)
	else:
		print("Enter correct gender!")
		exit(0)

def banner():
	banner = pyfiglet.figlet_format('WELCOME  TO\nWONDERLAND')
	print(banner)

start()
