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

# Traverses the given CourseList with a modified brute force algorithm
# Returns list containing all possible Schedule objects
def generate_possibilities(course_list):
    courses = course_list.get_courses() # Array of Course objects
    num_courses = courses.len() # Number of Courses being taken

    all_sections = [] # 2D array holding list of all sections for each course
    schedule_list = [] # Array holding all possible Schedules

    # populate the array with section data from provided CourseList
    for course in courses:
        all_sections.append(course.sections)

    # holds counters for each course's array, initialize all to 0
    counter_array = [0] * num_courses

    while True:
        # Create a new Schedule
        schedule = Schedule.Schedule()
        
        # Traverses all_sections to make a Schedule
        for x in range(num_courses):
            # TODO this breaks if the last section of a course has a conflict
            # Loop to ensure that a section is added from this course
            while True:
                # Pulls the next section for the course and attempts to add it
                section = all_sections[x][counter_array[x]]
                result = schedule.add_section(section)

                # Only loop if there was a conflict
                if not result:
                    # Increment counter for this Course to avoid future conflicts
                    counter_array[x] += 1
                else:
                    break

        # Add the new Schedule to the master list
        schedule_list.append(schedule)

        # TODO ok ive realized like, all of this increment shit fails several edge cases and my attempts to
        # rework it are not really panning out rn, ill fix it later lol
        # Increment counter_array as needed
        reset = False
        for x in reversed(range(num_courses)):
            counter = counter_array[x]
            num_sections = courses[x].sections.len()

            # No more sections for this course
            if (counter + 1) == num_sections:
                if not reset:
                    # Only ever want to increment 1 counter, even though sometimes you may need to reset more than 1
                    # Reset counter and increment previous counter to move to a different branch
                    counter_array[x] = 0
                    counter_array[x - 1] += 1
                    reset = True
            else:
                if not reset:
                    counter_array[x] += 1
                    reset = True
                break


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
