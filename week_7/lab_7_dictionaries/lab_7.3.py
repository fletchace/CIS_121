def mingrade(grades):
    smallest_grade = 100
    smallest_subject = ''
    for subject, grade in grades.items():
        if grade < smallest_grade:
            smallest_grade = grade
            smallest_subject = subject
    print(smallest_subject)

mingrade({"Physics":82,"Math":65,"History":75,"Biology":95,"English":87}) #"Math"
mingrade({"Chemistry":78,"Algebra":88,"History":72,"Geography":85}) #"History"
mingrade({"Art":90,"Music":92,"Drama":89}) #"Drama"