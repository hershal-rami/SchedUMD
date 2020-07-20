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
                    result = increment_counter[counter_array, courses, x]

                    if result:
                        # Last combination possible failed, we're done making Schedules
                        return
                else:
                    # Only loop if there was a conflict
                    break

        # Add the new Schedule to the master list
        schedule_list.append(schedule)

        # Recursive function to increment counter_array
        result = increment_counter[counter_array, courses, num_courses - 1]

        if result:
            return

# Increases last counter by 1, if it reaches the last section for that counter then increments the previous one recursively
# Returns True when there are no more course combinations to check, False otherwise
def increment_counter(counter_array, courses, current_index):
    counter = counter_array[current_index]
    num_sections = courses[current_index].sections.len()

    # Reached last section for this course
    if (counter + 1) == num_sections:
        if current_index == 0:
            # This is the first course, so we're done making Schedules
            return True
        
        # Reset current counter and increment previous one
        counter_array[current_index] = 0
        increment_counter(counter_array, courses, current_index - 1)
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

print("Ben:")
#print(benSc.get_courses()[1].sections[0].get_military_start_times())
#print(benSc.get_courses()[1].sections[0].get_military_end_times())
print(benSc.get_courses()[1].sections[1].get_meetings_booleans())
#print(benSc)

print("Hershal:")
#print(hershSc)