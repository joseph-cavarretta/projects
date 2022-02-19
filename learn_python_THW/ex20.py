#import sys library and from it the argv module
from sys import argv
#define the arguments
script, input_file = argv
#set a function named print_all that reads the file from the arguments and prints the contents
def print_all (f):
    print (f.read())
#set a function that seeks back to line 0 of the file.
def rewind(f):
    f.seek (0)
#set a function that prints one line at a time, and the number of the line.
def print_a_line (line_count, f):
    print (line_count, f.readline())
#create a variable names current file that opens the file from arguments
current_file = open(input_file)
#prints a string
print ("first let's print the whole file:\n")
#calls function ptint_all for the current file, which reads and prints the contents
print_all(current_file)
#prints a string
print ("Now let's rewind, kind of like a tape.")
#calls function rewind which takes the file back to line 0
rewind(current_file)
#prints a string
print ("Let's print three lines:")
#sets variable current_line equal to 1, then calls the print a line function which prints the selected line
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
