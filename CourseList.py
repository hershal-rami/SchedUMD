'''
Holds all Course objects for a CourseList.
Does not hold specific sections
'''

import Course

class CourseList:

    def __init__(self):
        self.courses = []   # Array of course objects

    def get_courses(self):
        return self.courses

    # Creates Course object out of String of course name
    def add_course(self, course):
        self.courses.append(Course.Course(course))

    def add_courses(self, courses):
        for c in courses:
            self.add_course(c)

    def remove_course(self, course):
        self.courses.remove(course)

    def remove_courses(self, courses):
        for c in courses:
            self.remove_course(c)

    def __str__(self):
        out = ""
        for course in self.courses:
            out += str(course) + "\n"

        return out