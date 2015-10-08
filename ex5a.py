his_name = 'vasanth'
his_age = 24
his_height = 173.0 # cm
his_height_in_inches = his_height / 2.54
his_weight = 63.0 # kg
his_weight_in_pounds = his_weight * 2.20462
his_eyes = 'black'
his_teeth = 'white'
his_hair = 'Black'

print "let's talk about %s." % his_name
print "He's %d inches(%d cm) tall." % (his_height_in_inches, his_height)
print "He's %d pounds(%d kg)heavy." % (his_weight_in_pounds, his_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (his_eyes, his_hair)
print "His teeth are usually %s depending on the coffee." % his_teeth

#this line is tricky, try to got it exactly right
print "His Body Mass Index is %d." %(his_weight_in_pounds/(his_height_in_inches**2)*703)
