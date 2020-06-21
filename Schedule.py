'''
Will hold all course objects for a schedule.
Making this a class will allow multiple schedules to be saved.
Can add/delete/specify courses within
'''

class Schedule:

    def __init__(self):
        self.courses = []      #Array of course objects

    def getCourses(self):
        return courses

    def addCourse(self, course):
        self.courses.append(course)

    def removeCourse(self, course):
        pass
        #remove course from array

    #can add other functions to manipulate array later



