'''
UMD Schedule Builder
https://github.com/hershal-rami/umd-schedule-builder

Authors:
Hershal Rami
Ben Davidson

6/20/2020
'''

def queryAllSections(courseID):
    #Make call to umd.io to get all sections with courseID
    print("")

def createSchedule(name):
    #Make new schedule with Id/name
    sch = schedule('name')

def addCourseToSchedule(schedule, course):
    schedule.addCourse(course)

def removeCourseFromSchedule(schedule, course):
    schedule.removeCourse(course)

def generatePossibilities(schedule):
    #Brute force schedules, return some data structure containing of them

#Will need functions to interface with webpage, 
#probably do this in JS and make calls to python to do backend

