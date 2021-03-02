import random 
import sys
import os
from time import sleep
import re

def type(words):
	for char in words:
	  sleep(0.1)
	  sys.stderr.write(char)

def type_speed(words, speed):
	for char in words:
	  sleep(speed)
	  sys.stderr.write(char)


def clear():
	os.system("clear")



inventory_list = []

global health
global enemy_health
global money
global turn_money

turn_money = 100


class Objects():
	@staticmethod
	def store():
		clear()
		global health
		global money
		global health_armor

		print("------- Store -------")
		print("-Equipment-\n")
		print("Sword (Lose Axe if in inventory) - 80")
		print("Axe (Lose Sword if in inventory) - 100")
		print("Horse - 450\n")
		print("-Armor-")
		print("Golden - 500")
		print("Silver - 400")
		print("Bronze - 200\n")
		print("-Food-")
		print("Meat - 100")
		print("Apple - 25")
		print("Beer - 20\n")
		print("Type 'L' to leave")

		while True:
			print("You have " + str(money) + " Gold Coins")
			store_prompt = raw_input("What would you like to buy today? > ")

			#buying sword
			if store_prompt.lower() == "sword":
				if "sword" in inventory_list:
					print("You already have this")

				elif money > 80:
					inventory_list.append("sword")
					money -= 80
					print("You have bought the sword")
					print("\n")

					#check if axe exists and remove
					if "axe" in inventory_list:
						inventory_list.remove("axe")

				else:
					print("You don't have enough money to buy this")

			#buying axe
			elif store_prompt.lower() == "axe":

				if "axe" in inventory_list:
					print("You already have this")
				elif money > 100:
					inventory_list.append("axe")
					money -= 100
					print("You have bought the axe")
					print("\n")

					#check if sword exists and remove
					if "sword" in inventory_list:
						inventory_list.remove("sword")

				else:
					print("You don't have enough money to buy this")

			#buy horse
			elif store_prompt.lower() == "horse":

				if "horse" in inventory_list:
					print("You already have a horse")
				elif money > 450:
					inventory_list.append("horse")
					money -= 450
					print("You have bought a horse")
					print("\n")

				else:
					print("You don't have enough money to buy this")

			#buy golden armor
			elif store_prompt.lower() == "golden armor" or store_prompt.lower() == "golden":
				if "golden" in inventory_list:
					print("You already have golden armor")
				elif money > 500:
					inventory_list.append("golden")
					money -= 500
					print("You have bought golden armor")
					print("\n")

					#remove other armor if in inventory
					if any("silver", "bronze") in inventory_list:
						inventory_list.remove("silver")
						inventory_list.remove("bronze")

				else:
					print("You don't have enough money to buy this")

			#buy silver armor		
			elif store_prompt.lower() == "silver armor" or store_prompt.lower() == "silver":
				if "silver" in inventory_list:
					print("You already have silver armor")
				elif money > 400:
					inventory_list.append("silver")
					money -= 400
					print("You have bought silver armor")
					print("\n")

					#remove other armor if in inventory
					if any("golden", "bronze") in inventory_list:
						inventory_list.remove("golden")
						inventory_list.remove("bronze")

				else:
					print("You don't have enough money to buy this")


			#buy bronze armor
			elif store_prompt.lower() == "bronze armor" or store_prompt.lower() == "bronze":
				if "bronze" in inventory_list:
					print("You already have bronze armor")

				elif money >= 200:
					inventory_list.append("bronze")
					money -= 200
					print("You have bought bronze armor")
					print("\n")

					#remove other armor if in inventory
					if any("silver", "golden") in inventory_list:
						inventory_list.remove("silver")
						inventory_list.remove("golden")

				else:
					print("You don't have enough money to buy this")

			#buy meat
			elif store_prompt.lower() == "meat":
				if "meat" in inventory_list:
					print("You already have meat")

				elif money >= 100:
					inventory_list.append("meat")
					money -= 100
					print("You have bought meat")
					print("\n")
				else:
					print("You don't have enough money to buy this")

			#buy apple
			elif store_prompt.lower() == "apple":
				if "apple" in inventory_list:
					print("You already have an apple")
				elif money >= 25:
					inventory_list.append("apple")
					money -= 25
					print("You have bought an apple")
					print("\n")

				else:
					print("You don't have enough money to buy this")

			#buy beer
			elif store_prompt.lower() == "beer":
				if "beer" in inventory_list:
					print("You already have beer")
				elif money >= 20:
					inventory_list.append("beer")
					money -= 20
					print("You have bought beer")
					print("\n")

				else:
					print("You don't have enough money to buy this")

			elif store_prompt.lower() == "l":
				break
				clear()
				print("You have left the store")
				print("\n")
			else:
				print("We don't currently have that in stock")

	@staticmethod
	def inventory():
		clear()
		global health

		if not inventory_list:
			print("\n")
			print("You have nothing in the inventory")
		else:
			while 1:
				Objects.info()
				print("----- Inventory -----")
				print("type 'use' then the food item to consume")
				print("L to leave")
				print("\n")
				for items in inventory_list:
					print(items)

				inventory_prompt = raw_input("> ")
				if inventory_prompt.lower() == "l":
					clear()
					break
				elif inventory_prompt.lower() == "use meat" and "meat" in inventory_list:
					print("You have eaten your meat")
					if health == 5:
						health += 0
					elif health == 4:
						health +=1
					elif health == 3 or health == 2 or health == 1:
						health +=2
					inventory_list.remove("meat")

				elif inventory_prompt.lower() == "use apple" and "apple" in inventory_list:
					print("You have eaten your apple")
					if health == 5:
						health += 0
					elif health == 4 or health == 3 or health ==2 or health ==1:
						health +=1
					inventory_list.remove("apple")

				elif inventory_prompt.lower() == "use beer" and "beer" in inventory_list:
					print("You have drinken your beer")
					if health == 5 or health == 4 or health == 3 or health == 2 or health == 1:
						health -= 1
					elif health == 0:
						health += 0
					inventory_list.remove("beer")

				elif inventory_prompt.lower() == "use meat" and "meat" not in inventory_list:
					print("You don't have meat in your inventory")
				elif inventory_prompt.lower() == "use apple" and "apple" not in inventory_list:
					print("You don't have an apple in your inventory")
				elif inventory_prompt.lower() == "use beer" and "beer" not in inventory_list:
					print("You don't have beer in your inventory")
				else:
					print("You can't consume that > ")


	@staticmethod
	def info():
		global health
		global energy_level

		energy_level = ""

		if health == 5:
			energy_level = "*****"
		elif health == 4:
			energy_level = "****"
		elif health == 3: 
			energy_level = "***"
		elif health == 2: 
			energy_level = "**"
		elif health == 1: 
			energy_level = "*"

		print("\n")
		print("-----------------------------------------------------------------")
		print("Health: " + energy_level)
		print(str(money) + " gold coins")

	@staticmethod
	def enemy_info():
		global enemy_health
		global enemy_energy_level

		if enemy_health == 5:
			enemy_energy_level = "*****"
		elif enemy_health == 4:
			enemy_energy_level = "****"
		elif enemy_health == 3: 
			enemy_energy_level = "***"
		elif enemy_health == 2: 
			enemy_energy_level = "**"
		elif enemy_health == 1: 
			enemy_energy_level = "*"
		print("-----------------------------------------------------------------")
		print("Enemy Health: " + enemy_energy_level)
		print("-----------------------------------------------------------------")



	@staticmethod
	def dead(return_function):
		clear()
		global money
		global health


		type("You have been killed")
		while 1: 
			dead_prompt = raw_input("Do you choose to continue the game? (Y,N) > ")
			if dead_prompt.lower() == "y":
				money -= 200
				health += 1
				return_function()
			elif dead_prompt.lower() == "n":
				Scenes.intro()
			else:
				print("> ")



	@staticmethod
	def help():
		print("-----------------------------------------------------------------")
		print("Type S to go to the Store")
		print("Type I to go to your Inventory")
		print("Type H for Help")
		print("Type E to Exit")
		print("Note - You recieve 100 gold coins for every decision you make")
		print("But lose 100 coins everytime you die")



class Actions():

	@staticmethod
	def fight(enemy, return_scene, next_scene):

		global health
		global enemy_health
		enemy_health = 5

		index = 0

		if "sword" in inventory_list:
			index += 2
		if "axe" in inventory_list:
			index += 3
		if "horse" in inventory_list:
			index += 1
		if "golden" in inventory_list:
			index += 2
		if "silver" in inventory_list:
			index += 1
		if "bronze" in inventory_list:
			index += 0
		if enemy == "Bandits":
			index+=2
		if enemy == "Dragon":
			index +=1
		if enemy == "Evil Wizard":
			index -= 1

		if index == 8:
			array = [1,2,3,4,5,6,7,8]
		elif index == 7:
			array = [1,2,3,4,5,6,7]
		elif index == 6:
			array = [1,2,3,4,5,6]
		elif index == 5:
			array = [1,2,3,4,5]
		elif index == 4:
			array = [1,2,3,4]
		elif index == 3:
			array = [1,2,3]
		elif index == 2:
			array = [1,2]
		elif index == 1:
			array = [1]
		elif index == 0:
			array = [0]
		elif index == -1:
			array = [0]	

		type_speed("-----------------------------------------------------------------\n", 0.01)
		type("You have chosen to fight the " + enemy + ".\n")

		while 1:
			clear()
			Objects.info()
			Objects.enemy_info()

			random_actions = random.sample(range(7), 2)
			actions = ["Swing at random", "Lunge at Enemy", "Swing directly at Head", "Swing at legs", "Jab at enemy", "Throw sword at enemy", "Drive for the chest of enemy", "Throw fists"]

			type("Choose an action: \n")
			type("A. " + actions[random_actions[0]] + "\n")
			type("B. " + actions[random_actions[1]] + "\n")
			fight_prompt = raw_input("(A, B) > ")


			#outcome of battle
			if health == 0:
				print("You have lost.")
				Objects.dead(return_scene)
				break

			elif enemy_health == 0: 
				break
				next_scene()

			if fight_prompt.lower() == "a":
				#type("You chose A")
				if random.randint(1,10) in array:
					enemy_health -= 1
				else:
					health -= 1

			elif fight_prompt.lower() == "b":
				#type("You chose B")
				if random.randint(1,10) in array:
					enemy_health -= 1
				else:
					health -= 1
			else:
				print("Try Again")








class Scenes():

	@staticmethod
	def intro():
		clear()
		print("\n")
		print("----------")
		type("Knightrise\n")
		print("----------")
		sleep(1)

		global health
		global enemy_health
		global money 

		health = 5
		enemy_health = 5
		money = 200
		inventory_list.append("horse")


		while 1:
			prompt = raw_input("Type 'Go' to begin > ")
			if prompt.lower() == "go":
				Scenes.scene_one()
				break
			elif prompt.lower() == "s":
				Objects.store()

			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "e":
				sys.exit(0)


	@staticmethod
	def scene_one():
		clear()
		global money
		global health

		print("-----------------------------------------------------------------")
		print("Type S to go to the Store")
		print("Type I to go to the Inventory")
		print("Type H for Help")
		print("Type E to Exit")
		print("-----------------------------------------------------------------")
		type("The Princess has been captured from the castle by the evil wizard.")
		print("The King has appointed you, his best man, to save her.")

		while 1:
			print("\n")
			prompt = raw_input("Do you accept this mission? (Y,N) > ")
			if prompt.lower() == "y":
				Scenes.scene_two()
				break
			elif prompt.lower() == "n":
				type("Goodbye Coward...\n")
				print("\n")
				Scenes.intro()				
				break
			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)


	@staticmethod
	def scene_two():
		clear()
		global money
		global health
		global turn_money

		if "horse" not in inventory_list:
			inventory_list.append("horse")


		Objects.info()
		print("-----------------------------------------------------------------\n")
		type("Upon leaving the castle, you travel for days on horseback.\n")
		type("All of a sudden you approach a fork.\n")
		type("A. To the left is the ancient dark forest\n")
		type("B. To the right is the stone road\n")


		while 1:
			prompt = raw_input("(A,B) > ")
			if prompt.lower() == "a":
				money += turn_money
				Scenes.scene_three_a()
				break
			elif prompt.lower() == "b":		
				money += turn_money
				Scenes.scene_three_b()
				break
			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)

	@staticmethod
	def scene_three_a():
		clear()
		global money
		global health
		global turn_money

		Objects.info()
		print("-----------------------------------------------------------------")
		type("Hours after traveling through the woods, you reach water.\n")
		type("Your horse neighs and stops.\n")
		type("A. Take horse through water\n")
		type("B. Abandon horse\n")

		while 1:
			prompt = raw_input("What do you choose? > ")
			if prompt.lower() == "a":
				money += turn_money
				Scenes.scene_four()
			elif prompt.lower() == "b":
				money += turn_money
				if "axe" in inventory_list:
					Objects.dead(Scenes.scene_three_a)
					inventory_list.remove("horse")



				else:
					Scenes.scene_four()
			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)


	@staticmethod
	def scene_three_b():
		clear()
		global money 
		global health
		global turn_money

		Objects.info()
		print("-----------------------------------------------------------------")
		type("Oh no!\n")
		type("Bandits have spotted you on the stone road and are approaching\n")
		type("A. Fight them\n")
		type("B. Flee\n")

		while 1:
			prompt = raw_input("What do you choose? > ")
			if prompt.lower() == "a":
				money += turn_money
				Actions.fight("Bandits", Scenes.scene_three_b, Scenes.scene_four)
				break
				#use current scene as parameter in fight() to move on to next scene

			elif prompt.lower() == "b":
				money += turn_money
				type("As you flee, you are shot in the head by a stray arrow.\n")
				Objects.dead(Scenes.scene_three_b)
			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)

	@staticmethod
	def scene_four():
		clear()
		global health
		global money
		global turn_money

		Objects.info()
		print("-----------------------------------------------------------------")
		type("After traveling for many more days, you have reached an Inn. \n")
		type("Do you choose to stay or continue on your journey? \n")

		while 1:
			prompt = raw_input("(Y,N) > ")
			if prompt.lower() == "y":
				money += turn_money

				if health == 5:
					health += 0
				elif health == 4 or health == 3 or health ==2 or health ==1:
					health +=1

				type("You have been charged 50 pieces of gold for your stay at the Inn \n")
				type("You continue on your journey well rested and content.\n")	
				money -= 50

				Scenes.scene_five()

			elif prompt.lower() == "n":
				money += turn_money

				type("You continue on your journey \n")
				Scenes.scene_five()

			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)

	@staticmethod
	def scene_five():
		clear()
		global health
		global money
		global turn_money

		Objects.info()
		print("-----------------------------------------------------------------")
		type("As you ride in the woods for many more days, you come across a loud sound \n")
		type("Snoring...\n")
		type("Oh No!\n")
		type("It is a sleeping Dragon!\n")
		type("All of a sudden, the sleeping Dragon wakes up and spots you. \n")
		type("A. Fight the Dragon \n")
		type("B. Flee \n")

		while 1:
			prompt = raw_input("(A,B) > ")
			if prompt.lower() == "a":
				money += turn_money

				Actions.fight("Dragon", Scenes.scene_five, Scenes.scene_six_a
				break


			elif prompt.lower() == "b":
				money += turn_money

				type("You have chosen to flee\n")
				Scenes.scene_six_b()

			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)



	@staticmethod
	def scene_six_a():
		clear()
		global health
		global money
		global turn_money


		#fly the dragon through the sky through left and right while skeletons shoot cannons at you
		print("-----------------------------------------------------------------\n")
		print("Having Defeated the Dragon...\n")
		print("it is now  tamed and will take you directly to the Evil wizards \n")
		print("-----------------------------------------------------------------")
		print("After a while of riding in the sky, you finally spot the Evil Wizard's Caste\n")
		print("But wait!\n")
		print("The Evil Wizard's Skeleton Army has spotted you...\n")
		print("You will have to successfully dodge the cannons that they shoot at you.\n")

		type_speed("-----------------------------------------------------------------", 0.01)

		type("The Skeletons are shooting their cannons at you.\n")

		turn = 0

		while 1:

			random_actions = random.sample(range(4), 2)
			actions = ["Swerve left", "Swerve right", "Pull up", "Plunge down", "Pull the Dragon back"]
			type("A. " + actions[random_actions[0]] + "\n")
			type("B. " + actions[random_actions[1]] + "\n")

			Objects.info()
			prompt = raw_input("(A, B) > ")

			#outcome of battle
			if health == 0:
				print("You have been shot out of the sky.\n")
				Objects.dead(Scenes.scene_six_a)
				break

			if turn == 6: 
				print("You have won!\n")
				money += turn_money
				Scenes.scene_seven()
				break


			if prompt.lower() == "a":
				type("You chose A")
				if random.randint(1,10) in (1,2,3,4,5,6,7,8):
					print("You have dodged a cannon\n")
					turn += 1
				else:
					print("You have been hit\n")
					health -= 1

			elif prompt.lower() == "b":
				type("You chose B")
				if random.randint(1,10) in (1,2,3,4,5,6,7,8):
					print("You have dodged a cannon\n")
					turn += 1
				else:
					print("You have been hit\n")
					health -= 1
			else:
				print("Try Again")




	@staticmethod
	def scene_six_b():
		clear()
		global health
		global money
		global turn_money

		#use luck to sneak around the walls
		print("-----------------------------------------------------------------\n")
		type("You have finally arrived at the Evil Wizard's Castle\n")
		type("But wait!\n")
		type("It is heavily guarded by his Skelelton Army.\n")
		type("You will need to sneak into the castle\n")
		type("and get to the top to confront the Evil Wizard.\n")

		type_speed("-----------------------------------------------------------------\n", 0.01)

		type("Choose your direction...")

		turn = 0

		while 1:
			clear()
			random_actions = random.sample(range(5), 2)
			actions = ["To the left", "To the right", "Up the stairs", "Into the dark room", "Straight ahead", "Climb the ladder"]
			type("A. " + actions[random_actions[0]] + "\n")
			type("B. " + actions[random_actions[1]] + "\n")

			Objects.info()
			prompt = raw_input("(A, B) > ")

			if health == 0:
				print("Oh no! You have been cornered by too many Skeletons and killed")
				Objects.dead(Scenes.scene_six_b)
				break

			if turn == 4: 
				print("You have successfully snuck past the Skeletons!")
				money += turn_money
				Scenes.scene_seven()
				break


			if prompt.lower() == "a":
				type("You chose A")
				if random.randint(1,10) in (1,2,3,4,5,6,7,8):
					turn += 1
				else:
					print("Oh no!")
					print("Skeletons have spotted you...")
					print("They attack and hurt you.")
					print("But you quickly kill them both before they attract attention.")
					health -= 1

			elif prompt.lower() == "b":
				type("You chose B")
				if random.randint(1,10) in (1,2,3,4,5,6,7,8):
					turn += 1
				else:
					print("Oh no!")
					print("Skeletons have spotted you...")
					print("They attack and hurt you.")
					print("But you quickly kill them both before they attract attention.")
					health -= 1
			else:
				print("Try Again")





	#final boss
	@staticmethod
	def scene_seven():
		clear()
		global health
		global money
		global turn_money
		
		print("-----------------------------------------------------------------\n")
		type("You reach the top of the tower where the Wizard stands.\n")
		type("And next to him...")
		type("The Princess!")
		type("She is pleading as the Wizard grabs her and threatens to throw her off the tower.")
		type("You pull out your weapon and the Wizard, his staff")
		type("Do you want to swing first at the Evil Wizard?")


		while 1:
			prompt = raw_input("(Y,N) > ")
			if prompt.lower() == "y":
				money += turn_money

				Actions.fight("Evil Wizard", Scenes.scene_seven)
				break
				Scenes.game_over()

			elif prompt.lower() == "n":
				money += turn_money

				type("The Evil Wizard charges at you with his staff.")

				Actions.fight("Evil Wizard", Scenes.scene_seven, Scenes.game_over)
				break

			elif prompt.lower() == "s":
				Objects.store()
			elif prompt.lower() == "h":
				Objects.help()
			elif prompt.lower() == "i":
				Objects.inventory()
			elif prompt.lower() == "e":
				sys.exit(0)


	@staticmethod
	def game_over():
		clear()
		type("You find a moment where the Wizard leaves his chest open.\n")
		type("You finally stab the wizard straight through the chest, piercing his heart")
		type("Standing on the edge of the tower, you kick him as he falls to his death.\n")
		print("-----------------------------------------------------------------\n")
		type(" VICTORY!!\n")
		type(" You have successfully killed the Evil Wizard and saved the Princess\n")
		type(" The grateful King has given you all riches and luxuries you could ever imagine\n")
		type("\n")
		type("GAME OVER\n")



	@staticmethod
	def credits():
		clear()
		print "\n"
		print "\n"
		print "------------------------------------------------------\n"
		print "           Created by Ali Kesserwani                  \n"
		print "------------------------------------------------------\n"
		print "\n"
		print "\n"

		time.sleep(2)
		Scenes.intro()




def gameloop():
	#start the game

	#put strings into a list in order to call the text universally with print and type
	Scenes.intro()

gameloop()











