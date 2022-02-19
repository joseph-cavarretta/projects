from sys import argv

script, filename = argv

print (f"We're going to read {filename}.")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN")

input ("?")

print ("Opening the file...")
txt = open(filename)

print ("Reading the file. Get ready!")
print (txt.read())
