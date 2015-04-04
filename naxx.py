from sys import exit
prompt = '> '
check = []

def dead(message):
	print message, "Good Job"
	exit(0)

def naxxarammas():
	print """
		Welcome to Naxxarammas 10 man!!\n
		Home of Kel\'Thuzad.!!\n
		Please select from the options below.\n
		\t 1. The Arachnid Quarter\n
		\t 2. The Plague Quarter\n
		\t 3. The Millitary Quarter\n
		\t 4. The Construct Quarter\n
		\t 5. Frostwing Lair\n
		"""
	choice = raw_input(prompt)
	try:
		choice = int(choice)
	except ValueError:
		print "Enter a Number."
	if choice not in range(1, 6):
		print " Wrong Choice."
		naxxarammas()
	if choice == 5 and len(check) < 4:
		print "You can't enter the lair without going through the other quarters"
		naxxarammas() 
	if choice == 1:
		arachnid_q()
	if choice == 2:
		plague_q()
	if choice == 3:
		millitary_q()
	if choice == 4:
		construct_q()

def arachnid_q():
	
	if "Arachnid" in check:
		print "You have already completed this quarter."
		naxxarammas()

	print """
		You enter the Arachnid Quarter, a pungent smell fills your breath.\n
		The entire place is covered in spider webs. Hit RETURN to proceed.\n
		"""
	raw_input(prompt)
	
	print """
		Across the hall, the giant spider Anub\'rekhan stands on top a trapdoor.\n
		You see a Sword and a bottle of bug spray on the floor.\n
		What do you do?
		"""
	while True:
	
		choice = raw_input(prompt)
	
		if "sword" in choice:
			dead("Anub\'rekhan covers you in a spray of spider web. You asphyxiate and die.")
		elif "bug spray" in choice:
			print " Anub\'rekhan goes blind.! You slip through the trap door. Good Job!. Hit RETURN to continue."
			raw_input(prompt)
			check.append("Arachnid") 
			print "The trap door leads you back to the temple entrance."
			naxxarammas()
		else:
			print "Sorry, I didn't catch that."



def plague_q():
	if "Plague" in check:
		print "You have already completed this quarter."
		naxxarammas()
	
	print """
		You enter the Plague Quarter. This placce makes you sick.\n
		You want to get out of here quickly.\n 
		Hit RETURN to continue.
		"""
	raw_input(prompt)
	
	print """ 
		Across the hall, you see Heigan the Unclean. Staring at you with plagued eyes.\n
		All along the hall there is eruption of ebon plague blight.\n
		You stand there confused. After a few minutes, you start to notice a pattern in the eruptions.\n
		You can either LEEROY into him or do the dance.\n
		"""

	while True:
	
		choice = raw_input(prompt)
		
		if "leeroy" in choice:
			dead("The ebon plague burns through skin and turns you into ashes within seconds.")
		elif "dance" in choice:
			print """
				You do the \'Heigan Dance\' and get to him.\n
				Heigan looks at you in disbelief, hands over his \'Dying Curse\'.\n
				He whispers into your year \' Good Luck You'll need it\'\n
				He then throws himself into his own creation and burns away.\n
				""" 
			check.append("Plague")
			print "The path loops back into the temple entrance. Hit RETURN to continue"
			raw_input(prompt)
			naxxarammas()
	
		else:
			print "I Didn't quite catch that."
	

def millitary_q():
	
	if "Millitary" in check:
		print "You have already completed this Quarter."
		naxxarammas()
	
	print """
		The constant sound of metal and screams of pain reaffirm your belief\n
		that you are indeed in the millitary quarter.\n
		This place gives you the chills.\n
		Hit RETURN to continue.\n
		"""
	raw_input(prompt)

	print """
		Instructor Razivious with this disciples stand in the middle\n
		of a sparring arena. Huge and Intimidanting, You don't want to pick a fight\n
		with this guy. Voices inside your head scream \"Man up and face him\"\n
		You then remember you can invoke the priest\'s blessing of mind control.\n
		What do you do?. The ball is in your court.\n
		"""
	
	while True:
		
		choice = raw_input(prompt)
		
		if "face" in choice:
			dead("Instructor razivious smashes you to pulp.")
		elif "mind control" in choice:
			print """
				You turn his disciples against him.\n
				You can see the pain of betrayal in his face as\n
				the disciples mercilessly pound on their master.\n
				You can almost feel for him.\n
				"""
			check.append("Millitary")
			print """
				As Razuvious dies, you start to run from this place through a\n
				narrow pathway which leads you into the Construct Quarter.\n
				"""
			construct_q()
		
		else:
			print "What are you saying mon'."

		

def construct_q():
	if "Construct" in check:
		print "But you've already completed this quarter. Let me take you back."
		naxxarammas()
	
	print "Entering the Construct quarter. Hit RETURN to continue"
	raw_input(prompt)
	
	print """
		The Construct Quarter, the place where you will\n
		face your toughest challenges yet.\n
		You see the abominable golem Patchwerk in front of you.\n
		He continuously keeps spewing green sludge in the shape of a cone.\n
		Hit RETURN to continue.\n
		"""
	raw_input(prompt)
	
	print """
		You notice that its the carrions inside his belly that keep him alive.\n
		To take him down you need to destroy the carrions.\n
		The only way to do that is to get close to him.\n
		Along the floor you see a shield and an axe.\n
		The shield bears the initials 'Methosian'. It probably belongs to a\n
		brave paladin who sacrificed himself for the group.\n
		You can dual wield. Shield on one hand and the axe on the other.\n
		Hit RETURN to continue.\n
		"""
	raw_input(prompt)

	print "Which one do you use, the shield or the axe?"
	
	while True:
		choice = raw_input(prompt)
		
		if "axe" in choice:
			dead("Patchwerk's spray annihilates you")
		elif "shield" in choice:
			print """ 
				Good Job!! You are now in the belly of patchwerk.\n
				Use your sword to kill the carrions.\n
				"""
			raw_input(prompt)
			print """
				As patchwerk falls, you feel the presence of those brave souls\n
				who were victims of patchy's fury. You get of the place and find yourself\n
				in the temple entrance.\n
				"""
			check.append("Construct")
			naxxarammas()
		else:
			print "Be more clear dude!"

			
				

naxxarammas()
	
