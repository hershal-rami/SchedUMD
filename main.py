'''
UMD Schedule Builder
https://github.com/hershal-rami/umd-schedule-builder

Authors:
Hershal Rami
Ben Davidson

6/20/2020
'''

import requests
import Course
import CourseList

def generate_possibilities(course_list):
    #Brute force schedules, return some data structure containing of them
    schedule_list = []  # List containing all possible schedules

    pass

benSc = CourseList.CourseList()
hershSc = CourseList.CourseList()

benCourses = ['CMSC351', 'CMSC216', 'HACS200', 'MATH241', 'CMSC389O', 'GEOG170']
hershCourses = ['CMSC351', 'CMSC330', 'STAT400', 'HACS200', 'HACS208N', 'CMSC389O']

benSc.add_courses(benCourses)
hershSc.add_courses(hershCourses)

print("Ben:")
#print(benSc.get_courses()[1].sections[0].get_military_start_times())
#print(benSc.get_courses()[1].sections[0].get_military_end_times())
print(benSc.get_courses()[1].sections[1].get_meetings_booleans())
#print(benSc)

print("Hershal:")
#print(hershSc)
