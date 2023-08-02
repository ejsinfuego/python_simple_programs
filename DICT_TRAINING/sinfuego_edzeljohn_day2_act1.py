noun1 = str(input("New Noun 1: "))
noun2 = str(input("New Noun 1: "))
adjective1 = str(input("New Adjective 1: "))
adjective2 = str(input("New Adjective 2: "))

lyrics = """Everybody said we'd be together forever
But I know that I never wanna settle down
Come around, break up the love like LEGO now
Never wanna turn into another like you
Sleep with my thoughts, dance with my views
Everything's great, not everything's sure
But you live in your halls and I live in a tour bus"""

newNoun1 = lyrics.replace("I", noun1, 1)
newNoun2 = newNoun1.replace("you", noun2, 1)
adjective1 = newNoun2.replace("great", adjective1)
adjective2 = adjective1.replace("sure", adjective2)

print("Old lyrics: " + lyrics)

print("New lyrcis: " + adjective2)


