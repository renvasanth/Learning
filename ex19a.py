def student(name, age, native):
    print "%s, %d years old came from %s." % (name, age, native)


name = raw_input("Enter name: ")
age = int(raw_input("Enter age: "))
native = raw_input("Enter native: ")
student(name, age, native)

from sys import argv
kkk, name, age, native = argv
student(name, int(age), native)
