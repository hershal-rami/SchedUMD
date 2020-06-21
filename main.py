'''
UMD Schedule Builder
https://github.com/hershal-rami/umd-schedule-builder

Authors:
Hershal Rami
Ben Davidson

6/20/2020
'''

import requests
import Schedule

def queryById(courseID):
    #Make call to umd.io to get all sections with courseID
    r = requests.get('https://api.umd.io/v1/courses/' + courseID)
    return r

def addCourseToSchedule(schedule, course):
    schedule.addCourse(course)

def removeCourseFromSchedule(schedule, course):
    schedule.removeCourse(course)

def generatePossibilities(schedule):
    #Brute force schedules, return some data structure containing of them
    pass

sch = Schedule.Schedule()
addCourseToSchedule(sch, 'CMSC351')
addCourseToSchedule(sch, 'CMSC216')
addCourseToSchedule(sch, 'HACS200')

print(sch.courses)
print("=======================")

for course in sch.courses:
    print(queryById(course).json()[0].get("course_id"))
