from sys import argv

script, user_name, friend_name = argv
ask = '>'

print "Hi %s and %s, I'm the %s script." % (user_name, friend_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s and %s?" % (user_name, friend_name)
likes = raw_input(ask)

print "Where do you live %s?" % user_name
lives = raw_input(ask)
print "and you %s?" % friend_name
lives1 = raw_input(ask)

print "what kind of computer do you have?"
computer = raw_input(ask)
print """
Alright, so you said %r about liking me.
You live in %r and %r. Not sure where those are.
And you have a %r computer. Nice.
""" % (likes, lives, lives1, computer)
