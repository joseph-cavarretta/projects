# defines how many types of people variable
types_of_ppl = 10
# defines x as a formatted string
x = f"there are {types_of_ppl} types of people"
#defins variable binary
binary = "binary"
# defines variable do_not
do_not = "don't"
#defines variable y as a formatted string with 2 strings within it
y = f"those who know {binary} and those who {do_not}"
#prints x, y variables
print (x)
print (y)
#prints formatted strings with strings x,y within them
print (f"I said: {x}")
print (f"I also said: '{y}'")
# defines varable hilarous as False
hilarious = False
#defines variable joke eval as a string with brackets where a foratted variable can be added
joke_evaluation = "Isnt't that joke so funny?! {}"
#prints variable joke eval with a formatted hilarious variable
print (joke_evaluation.format(hilarious))

w = "This is the left side of .."
e = "a string with a right side."
#concatenates strings w and e
print (w + e)
