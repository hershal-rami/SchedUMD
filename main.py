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

'''
# Traverses the given CourseList with a modified brute force algorithm
# Returns list containing all possible Schedule objects
def generate_possibilities(course_list):
    global inc
    inc = 0
    courses = course_list.get_courses() # Array of Course objects
    num_courses = len(courses)

    schedule_list = [] # Array holding all possible Schedules

    # Holds counters for each course's array, initialize all to 0
    counter_array = [0] * num_courses

    arrayStr = "["
    for i in range(num_courses):
        arrayStr += str(len(courses[i].sections)) + "  (" + courses[i].course_id + ")"
        if (i != num_courses-1):
            arrayStr += ",\n"

    arrayStr += "]"
    print("Counter array max values: \n" + arrayStr)

    while True:
        # Create a new Schedule
        schedule = Schedule.Schedule()
        
        # Traverses all courses to make a Schedule
        for course_idx in range(num_courses):
            # Continues adding sections until one works
            while True:
                # Pulls the next section for the course and attempts to add it
                counter = counter_array[course_idx]
                section = courses[course_idx].sections[counter]
                success = schedule.add_section(section)

                if not success:
                    # Reached last section for this course
                    if (counter + 1) == len(courses[course_idx].sections):
                        # Updates entire schedule to move to a different branch of sections
                        finished = update_schedule()
                        break
                    else:
                        # Increment counter for this Course to avoid future conflicts
                        finished = increment_counter(counter_array, courses, course_idx)

                    if finished:
                        # Last combination possible failed, we're done making Schedules
                        return schedule_list
                else:
                    break
        
        # Add the new Schedule to the master list
        schedule_list.append(schedule)

        # Recursive function to increment counter_array
        finished = increment_counter(counter_array, courses, num_courses - 1)

        # No more schedules to make, so return master list
        if finished:
            return schedule_list

# Updates given schedule to match sections corresponding to the counter_array. If a conflict is found, it iterates
# and recurses until success. Returns True if there are no more schedules to be made, False otherwise
def update_schedule(schedule, counter_array, courses, index):
    # Increment counter past failed combination
    finished = increment_counter(counter_array, courses, index)
    
    # Return if the last possible combination failed
    if finished:
        return True

    schedule.clear()

    # Loop through all courses
    num_courses = len(courses)
    for course_idx in range(num_courses):
        counter = counter_array[course_idx]
        section = courses[course_idx].sections[counter]
        
        success = schedule.add_section(section)

        # Found another conflict, recurse to account for it
        if not success:
            return update_schedule(schedule, counter_array, courses, index)

    # Made a schedule successfully, we are not done yet
    return False
'''

inc = 0
# Traverses the given CourseList with a modified brute force algorithm
# Returns list containing all possible Schedule objects
def generate_possibilities(course_list):
    global inc
    inc = 0

    courses = course_list.get_courses() # Array of Course objects
    num_courses = len(courses)

    schedule_list = [] # Array holding all possible Schedules

    # Holds counters for each course's array, initialize all to 0
    counter_array = [0] * num_courses

    arrayStr = "["
    for i in range(num_courses):
        arrayStr += str(len(courses[i].sections)) + "  (" + courses[i].course_id + ")"
        if (i != num_courses - 1):
            arrayStr += ",\n"
    arrayStr += "]"
    print("Counter array max values: \n" + arrayStr)

    while True:
        # Returns a unique schedule on success, False on failure, and 'finished' if no more schedules to be made
        schedule = make_schedule(counter_array, courses, num_courses)

        # Last possible combination failed
        if schedule == 'finished':
            return schedule_list

        # Schedule object should be evaluated to True
        if not schedule:
            continue

        # Add new schedule to master list
        schedule_list.append(schedule)

        # Returns True if done making Courses, otherwise increments counter_array
        finished = increment_counter(counter_array, courses, num_courses - 1)

        # No more schedules to make, so return master list
        if finished:
            return schedule_list

# Attempts to make a single schedule and return it. If there is a major conflict, it returns false. If there
# are no more possible combinations, it returns 'finished.'
def make_schedule(counter_array, courses, num_courses):
    # Create a new Schedule
    schedule = Schedule.Schedule()

    last_section = False

    # Traverses all courses to make a Schedule
    for course_idx in range(num_courses):
        # Continues looping until a section works
        while True:
            # Pulls the next section for the course and attempts to add it
            counter = counter_array[course_idx]
            section = courses[course_idx].sections[counter]
            success = schedule.add_section(section)

            if not success:
                # Reached last section for this course
                if (counter + 1) == len(courses[course_idx].sections):
                    last_section = True

                # Increment counter for this Course to avoid future conflicts
                finished = increment_counter(counter_array, courses, course_idx)

                if finished:
                    # Last combination possible failed, we're done making Schedules
                    return "finished"

                # Main loop will continue and try again with the new iterated values
                if last_section:
                    return False
            else:
                break
    
    # Successfully made a schedule
    return schedule
    
# By default increases last counter by 1. If there are no more sections for a counter, then increments the previous one
# recursively. Returns True when there are no more course combinations possible (i.e. first course runs out of sections)
# Returns False otherwise
def increment_counter(counter_array, courses, course_idx):
    global inc
    inc += 1

    counter = counter_array[course_idx]
    num_sections = len(courses[course_idx].sections)

    # Reached last section for this course
    if (counter + 1) == num_sections:
        if course_idx == 0:
            # This is the first course, so we're done making Schedules
            return True
        
        # Reset current counter and increment previous one
        counter_array[course_idx] = 0
        return increment_counter(counter_array, courses, course_idx - 1)
    else:
        # Increment current counter and return to main loop
        counter_array[course_idx] += 1
        return False

'''
benSc = CourseList.CourseList()
hershSc = CourseList.CourseList()

benCourses = ['CMSC351', 'CMSC216', 'HACS200', 'MATH241', 'CMSC389O', 'GEOG170']
hershCourses = ['CMSC351', 'CMSC330', 'STAT400', 'HACS200', 'HACS208N', 'CMSC389O']

benSc.add_courses(benCourses)
hershSc.add_courses(hershCourses)

print("Running generate on benSc...")
t0 = time.time()
all_schedules = generate_possibilities(benSc)
t1 = time.time()
total = t1 - t0
print(str(total)[:5] + " seconds to run")
print(str(inc) + " increment calls")
print(str(len(all_schedules)) + " schedules made!\n")

print("Running generate on hershSc...")
t0 = time.time()
all_schedules = generate_possibilities(hershSc)
t1 = time.time()
total = t1 - t0
print(str(total)[:5] + " seconds to run")
print(str(inc) + " increment calls")
print(str(len(all_schedules)) + " schedules made!")
'''
testSc = CourseList.CourseList()
testCourses = ['MATH406', 'HACS100']
testSc.add_courses(testCourses)
print("Running generate on testSc...")
t0 = time.time()
all_schedules = generate_possibilities(testSc)
t1 = time.time()
total = t1 - t0
print(str(total)[:5] + " seconds to run")
print(str(inc) + " increment calls")
print(str(len(all_schedules)) + " schedules made!")

for schedule in all_schedules:
    print(schedule)
