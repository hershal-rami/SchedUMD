'''
Will hold all course objects for a schedule.
Making this a class will allow multiple schedules to be saved.
Can add/delete/specify courses within
'''

class Schedule:

    def __init__(self, courses):
        self.courses = courses      #Array of course objects

    def getCourses(self):
        #return courses array
        #might not need this, can just do schedule.courses

    def addCourse(self, course):
        #add course to array

    def removeCourse(self, course):
        #remove course from array

    #can add other functions to manipulate array later



