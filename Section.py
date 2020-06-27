'''
Class to house all data for a section of a Course
:
i.e. location, time, professor, etc. for CMSC132-0101
'''

import requests, math

class Section:

    def __init__(self, section_data):
    
        self.section_id = section_data.get("section_id");     # Course code plus sectionID ("CMSC250-0101")
        self.number = section_data.get("number")              # Second half of sectionID (0101)
        self.instructors = section_data.get("instructors")    # Array of professor names for section (e.g. {"Yoon", "Shankar"})
        self.seats = section_data.get("seats")                # Total number of seats for section
        self.open_seats = section_data.get("open_seats")      # Number of remaining seats
        self.waitlist = section_data.get("waitlist")          # Number of people on the waitlist
        
        self.meetings = section_data.get("meetings")          # Dictionary housing meeting info for the section
           
            # Dictionary defined as follows                                        
                # "days" -> string         (e.g.) MWF, MW
                # "room" -> string         (e.g.) 0324, 2118
                # "building" -> string     (e.g.) IRB, CSI
                # "classtype" -> string    (e.g.) Lecture, Discussion
                # "start_time" -> string   (e.g.) 3:00pm, 12:00pm
                # "end_time" -> string     (e.g.) 3:50pm, 12:50pm

    # Returns start times of all meetings in an array
    def get_start_times(self):
        start_times = []
        for meeting in self.meetings:
            start_times.append(meeting.start_time)
        return start_times

    # Returns end times of all meetings in an array
    def get_end_times(self):
        end_times = []
        for meeting in self.meetings:
            end_times.append(meeting.end_time)
        return end_times

    # Converts 12 hour time to military
    def get_military_time(self, time):
        colon_idx = time.find(":")
        hour = int(time[:colon_idx])
        meridian = time[(colon_idx + 3):]   # am or pm

        # Accounts for 12:00am -> 0000 case
        if hour == 12:
            hour = 0

        # If past noon, add 12
        if meridian.lower() == 'pm':
            hour += 12
        else:
            if hour < 10:
                hour = str(0) + str(hour)

        hour = str(hour) + (time[(colon_idx + 1):(colon_idx + 3)])
        return hour
        
    # Returns start time of all meetings in military time
    def get_military_start_times(self):
        military_times = []
        for meeting in self.meetings:
            military_times.append(self.get_military_time(meeting.get("start_time")))

        return military_times

    # Returns end time of all meetings in military time
    def get_military_end_times(self):
        military_times = []
        for meeting in self.meetings:
            military_times.append(self.get_military_time(meeting.get("end_time")))

        return military_times
    
    def scale_military_time(self, time):
        hour = str(time)[:2]
        minute = math.ceil(int(str(time)[2:]) * 10/6)
        if(minute < 10):
            minute = "0" + str(minute)

        return hour + str(minute)
    
    # Returns 5x68 2d array of booleans. M-F, 6am-11pm, 15min increments
    def get_meetings_booleans(self):
        out = []
        for i in range(5):
            out.append([])
            for j in range(68):
                out[i].append(False)
        
        for meeting in self.meetings:

            days = []
            if "M" in meeting.get("days"):
               days.append(0)
            if "u" in meeting.get("days"):
               days.append(1)
            if "W" in meeting.get("days"):
               days.append(2)
            if "h" in meeting.get("days"):
               days.append(3)
            if "F" in meeting.get("days"):
               days.append(4)
            
            start = int(self.get_military_time(meeting.get("start_time")))
            start = int(self.scale_military_time(start))
            end = int(self.get_military_time(meeting.get("end_time")))
            end = int(self.scale_military_time(end))
            
            start = math.ceil((start / 25) - 24)
            end = math.ceil((end / 25) - 24)
            diff = end-start

            for day in days:
                for i in range(diff):
                    out[day][start+i] = True

        return out
    
    def __str__(self):
        out = ""

        out += "@@@@" + self.section_id + "@@@@\n"
        out += "\n----instructors----\n"
        for instructor in self.instructors:
            out += "- Instructor: " + instructor
        out += "\n----seats----\n"
        out += self.seats
        out += "\n----open_seats----\n"
        out += self.open_seats
        out += "\n----waitlist----\n"
        out += self.waitlist
        out += "\n----meetings----\n"
        for meeting in self.meetings:
            out += "\n$$$$ MEETING $$$$\n"
            out += "--days--\n"
            out += meeting.get("days")
            out += "\n--room--\n"
            out += meeting.get("room")
            out += "\n--building--\n"
            out += meeting.get("building")
            out += "\n--classtype--\n"
            out += meeting.get("classtype")
            out += "\n--start_time--\n"
            out += meeting.get("start_time")
            out += "\n--end_time--\n"
            out += meeting.get("end_time")
        out += "\n@@@END SECTION@@\n"
        return out


            

