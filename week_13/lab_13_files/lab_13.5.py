poopy_poem = open("week_13\\lab_13_files\\thePoopyPoem.txt", "r")

dih = {}
words = poopy_poem.read()
poopy_poem.close()

words = words.lower()
words = words.split()

for word in words:
    if word in dih:
        dih[word] += 1
    else:
        dih[word] = 1

print(dih)