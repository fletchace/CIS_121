my_words = open("week_13\\lab_13_files\\MyWords.txt", "r")
new_words = open("week_13\\lab_13_files\\NewWords.txt", "w")

lyst = []
for line in my_words.readlines():
    word = line.strip()
    if len(lyst) != 5:
        lyst.append(word)
        if len(lyst) == 5:
            new_words.write(str(lyst) + "\n")
            lyst = []