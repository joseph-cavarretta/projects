tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

universal_cat = "{}"

print (universal_cat.format("\tI'm tabbed in"))
print (universal_cat.format("I'm split\non a line"))
print (universal_cat.format("I'm \\ a \\ cat"))
print (universal_cat.format(fat_cat))
