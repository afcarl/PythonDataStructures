"""
correct sematics, bad syntax:

I ran walked side ways hoping to run along your hands.

Correct syntax, bad semantics:

I smiled into the cat.

"""

# Below is a simple program that writes syntactically inaccurate sentences.

from random import choice
nouns = ["Eric","cat","dog","snowflake","snowman","cheese","Noam"]
verbs = ["Ran","walked","ran","running","playing","jumping","laughing"]

sentence = ""
for i in xrange(15):
    if i%2 == 0:
        sentence += choice(noun)
    else:
        setence += choice(verb)

print sentence+"."
