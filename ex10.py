# Something about escape sequences. Escape sequence as the name suggests is the way how you can escape the character sequence. 
tabby_cat = "\tI'm tabbed in." # this is for introducing tab space in the string
persian_cat = "I'm split\non a line." # newline escape sequence.
backslash_cat = "I'm \\ a \\ cat." # for printing out a backslash.

escseq = "I am a bad man \a as\bdfg \fhij \nklm \rnop \tqrs Please help." # \r and \n give the same output. I am not sure of what the difference between them is. I will learn.

fat_cat = """
I'll do a list
\t* Catfood
\t* Fisies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print escseq
