import sys

import random

ans = True

while ans:

	question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")

 	answers = random.randint(1,8)

	if question == "":

		sys.exit()

	elif answers == 1:

		print "it is certain"

	elif answers == 2:

		print "outlook good"

	elif answers == 3:

		print " you may rely on it"

	elif answers == 4:

		print "ask again later"

	elif answers == 5:

		print "concentrate and ask again"

	elif answers == 6:

 		print "reply hazy, try again"

	elif answers == 7:

		print "my reply is no"

	elif answers ==8:

		print "my sources say no"







