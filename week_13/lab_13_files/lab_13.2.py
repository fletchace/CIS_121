this_file = open("week_13\\lab_13_files\\thisFile.txt", "r")
that_file = open("week_13\\lab_13_files\\thatFile.txt", "w")

lisp = []
for line in this_file.readlines():
    lines = line.strip()
    lisp.append(lines)

for thang in lisp[::2]:
    that_file.write(thang + "\n")

this_file.close()
that_file.close()