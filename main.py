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

'''
benSc = CourseList.CourseList()
hershSc = CourseList.CourseList()

benCourses = ['CMSC351', 'CMSC216', 'HACS200', 'MATH241', 'CMSC389O', 'GEOG170']
hershCourses = ['CMSC351', 'CMSC330', 'STAT400', 'HACS200', 'HACS208N', 'CMSC389O']

benSc.add_courses(benCourses)
hershSc.add_courses(hershCourses)

print("Ben:")
print(benSc)

print("Hershal:")
print(hershSc)
'''

'''
testSc = CourseList.CourseList()
testSc.add_course('ENEE200')
print(testSc)
'''

course = Course.Course('ENEE200')
print(course.get_section_data('0101'))