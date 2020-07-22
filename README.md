# SchedUMD
Set-Up:
-Remove old versions of Python and install Python 3.8.3
-Use pip to install requests
    `pip install requests` for Windows
    `sudo pip install requests` for OSX/Linux

Useful Links:
https://umd.io/
https://jasonpark.me/gt-scheduler/
https://api.umd.io/v1/courses

To Do:
-Replace heat map conflict checking with hashsets or some other method
-Create front-end to manipulate the class data
-Cut down number of redudanct sections (i.e. same times but different discussions/rooms)
-Add ability to filter out undesired schedules based on time, location, professor, etc.
-Use Threading to make API calls as the user selects a course in the dropdown
-Add additional options to filter out undesired schedules
-Pick classes closest to a certain location/optimizing schedules for distance
-Filter out undesired buildings
-Update README and github repo once complete