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

def query_by_Id(courseID):
    #Make call to umd.io to get all sections with given courseID
    r = requests.get('https://api.umd.io/v1/courses/' + courseID)
    return r

def add_course_to_schedule(schedule, course):
    schedule.add_course(course)

def remove_course_from_schedule(schedule, course):
    schedule.remove_course(course)

def generate_possibilities(schedule):
    #Brute force schedules, return some data structure containing of them
    pass

'''
sch = Schedule.Schedule()

add_course_to_schedule(sch, 'CMSC351')
add_course_to_schedule(sch, 'CMSC216')
add_course_to_schedule(sch, 'HACS200')

print(sch.courses)
print("=======================")

for course in sch.courses:
    print(query_by_Id(course).json()[0].get("course_id"))
'''
sch = Schedule.Schedule()

print("Please enter a course ID. Enter a blank line to finish.")

while(True):
    course_id = input("Course ID: ")

    if(not course_id): # empty string is false
        break

    sch.add_course(course_id)

print(sch.get_courses())

