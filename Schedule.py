'''
Will hold all course objects for a schedule.
Making this a class will allow multiple schedules to be saved.
Can add/delete/specify courses within
'''

class Schedule:

    def __init__(self):
        self.courses = []      #Array of course objects

    def __str__(self):
        out = ""
        for course in self.courses:
            out += course + "\n"

        return out

    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    #can add other functions to manipulate array later



