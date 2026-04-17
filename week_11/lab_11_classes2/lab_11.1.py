class Student:
    def __init__(self, name, major):
        # Class Variables
        self._name = name
        self._major = major

    def get_major(self):
        return self._major

    def set_major(self, new_major):
        self._major = new_major
    
    def __str__(self):
        return f"Student Name: {self._name} Major: {self._major}"


class Course:
    def __init__(self, name, number):
        self._course_name = name
        self.course_number = number
        # = [] means a empty list
        self.studnets = []

    def get_number(self):
        return self.course_number
    
    def set_number(self, num):
        self.course_number = num

    def add_student(self, student1:Student):
        self.studnets.append(student1)

    def show_student_enrollment(self):
        for student in self.studnets:
            print(student)
    
    def __str__(self):
        return f"Course: {self._course_name} {self.course_number}. There is {len(self.studnets)} students in the course."

goodStudent1 = Student("Reese", "DoingNothing101")
bad_student_1 = Student("Rebecca", "History")
very_bad_student = Student("Mason", "Poopology")

best_course = Course("CIS", 121)
best_course.add_student(bad_student_1)
best_course.add_student(very_bad_student)
best_course.show_student_enrollment()
print(best_course)