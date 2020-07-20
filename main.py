'''
SchedUMD
https://github.com/hershal-rami/SchedUMD

Authors:
Hershal Rami
Ben Davidson

6/20/2020
'''

import requests
import time
import Schedule
import Course
import CourseList

# Traverses the given CourseList with a modified brute force algorithm
# Returns list containing all possible Schedule objects
def generate_possibilities(course_list):
    courses = course_list.get_courses() # Array of Course objects
    num_courses = len(courses)

    all_sections = [] # 2D array holding list of all sections for each course
    schedule_list = [] # Array holding all possible Schedules

    # Populate the array with section data from provided CourseList
    for course in courses:
        all_sections.append(course.sections)

    # Holds counters for each course's array, initialize all to 0
    counter_array = [0] * num_courses

    while True:
        # Create a new Schedule
        schedule = Schedule.Schedule()
        
        # Traverses all_sections to make a Schedule
        for x in range(num_courses):
            # Loop to ensure that a section is added from this course
            while True:
                # Pulls the next section for the course and attempts to add it
                section = all_sections[x][counter_array[x]]
                success = schedule.add_section(section)

                if not success:
                    # Increment counter for this Course to avoid future conflicts
                    result = increment_counter(counter_array, courses, x)

                    if result:
                        # Last combination possible failed, we're done making Schedules
                        return schedule_list
                else:
                    # Only loop if there was a conflict
                    break

        # Add the new Schedule to the master list
        schedule_list.append(schedule)

        # Recursive function to increment counter_array
        result = increment_counter(counter_array, courses, num_courses - 1)

        # No more schedules to make, so return master list
        if result:
            return schedule_list

# By default increases last counter by 1. If there are no more sections for a counter, then increments the previous one
# recursively. Returns True when there are no more course combinations possible (i.e. first course runs out of sections)
# Returns False otherwise
def increment_counter(counter_array, courses, current_index):
    counter = counter_array[current_index]
    num_sections = len(courses[current_index].sections)

    # Reached last section for this course
    if (counter + 1) == num_sections:
        if current_index == 0:
            # This is the first course, so we're done making Schedules
            return True
        
        # Reset current counter and increment previous one
        counter_array[current_index] = 0
        return increment_counter(counter_array, courses, current_index - 1)
    else:
        # Increment current counter and return to main loop
        counter_array[current_index] += 1
        return False


benSc = CourseList.CourseList()
hershSc = CourseList.CourseList()

benCourses = ['CMSC351', 'CMSC216', 'HACS200', 'MATH241', 'CMSC389O', 'GEOG170']
hershCourses = ['CMSC351', 'CMSC330', 'STAT400', 'HACS200', 'HACS208N', 'CMSC389O']

benSc.add_courses(benCourses)
hershSc.add_courses(hershCourses)

t0 = time.time()
all_schedules = generate_possibilities(benSc)
t1 = time.time()
total = t1 - t0
print(total)

t0 = time.time()
all_schedules = generate_possibilities(hershSc)
t1 = time.time()
total = t1 - t0
print(total)