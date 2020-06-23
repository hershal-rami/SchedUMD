'''
Class to house all data for a section of a Course

i.e. location, time, professor, etc. for CMSC132-0101
'''

import requests

class Section:

    def __init__(self, section_data):
    
        self.section_id = section_id;              # Course code plus sectionID ("CMSC250-0101")
        self.number = r.get("number")              # Second half of sectionID (0101)
        self.instructors = r.get("instructors")    # Array of professor names for section (e.g. {"Yoon", "Shankar"})
        self.seats = r.get("seats")                # Total number of seats for section
        self.open_seats = r.get("open_seats")      # Number of remaining seats
        self.waitlist = r.get("waitlist")          # Number of people on the waitlist
        
        self.meetings = section_data.get("meetings")          # Dictionary housing meeting info for the section
           
            # Dictionary defined as follows                                        
                # "days" -> string         (e.g.) MWF, MW
                # "room" -> string         (e.g.) 0324, 2118
                # "building" -> string     (e.g.) IRB, CSI
                # "classtype" -> string    (e.g.) Lecture, Discussion
                # "start_time" -> string   (e.g.) 3:00pm, 12:00pm
                # "end_time" -> string     (e.g.) 3:50pm, 12:50pm
                

    def __str__(self):
        out = ""

        out += "@@@@" + self.number + "@@@@\n"
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
            out += meeting.get("end_time")
            out += "\n--end_time--\n"
            out += meeting.get("start_time")
        out += "@@@END SECTION@@\n"
        return out


            

