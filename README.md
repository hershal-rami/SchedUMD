# umd-schedule-builder
Set-Up:
-Remove old versions of Python and install Python 3.8.3
-Use pip to install requests
    `pip install requests` for Windows
    `sudo pip install requests` for OSX/Linux


General Plan:
-Use python
-Only need 1 file for collecting data and outputting schedules
-Potentially another for communicating with the front-end

Useful Links:
https://umd.io/
https://jasonpark.me/gt-scheduler/

To Do:
-Get the data from Testudo
-Write the brute force algorithm to create all schedules
-Output schedule info as text to test
-Create front-end to manipulate the class data
-Add additional options to filter out undesired schedules
-Pick classes closest to a certain location/optimizing schedules for distance
-Filter out undesired buildings
-Write README once complete


Get a course from the user
Get a list of all sections for that course
print out all sections with info


-------------------
user will give us a list of courses they want on their schedule
we get the list of sections for each course from umd.io
-store a list of Courses and Course object stores a list of sections
-create a list of Schedules, where each Schedule object is a possibility that stores a list of sections