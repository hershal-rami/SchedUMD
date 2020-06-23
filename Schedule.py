'''
Will hold all course objects for a schedule.
Making this a class will allow multiple schedules to be saved.
Can add/delete/specify courses within
'''

import Course

class Schedule:

    def __init__(self):
        self.courses = []      #Array of course objects

    def __str__(self):
        out = ""
        for course in self.courses:
            out += str(course) + "\n"

        return out

    def get_courses(self):
        return self.courses

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
    #can add other functions to manipulate array later



