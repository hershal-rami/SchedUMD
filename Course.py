'''
Class to house data on all sections of a course

i.e. all CMSC351 sections
'''

class Course:

    def __init__(self, course, sectionID, semester, number, 
                seats, meetings, open_seats, waitlist, instructors):
                self.course = course              #The associated course id (ENGL101)
                self.sectionID = sectionID        #Unique course identifier (ENGL101-0101)
                self.semester = semester          #Numeric representation YYYYMM (202001)
                self.number = number              #Second half of secitonID (0101)
                self.seats = seats                #Total number of seats for section
                self.meetings = meetings          #Array housing dictionaries of meeting info for section
                                                
                                                #each entry in array represents a meeting on weekly basis
                                                #dictionary defined as follows
                                                #        "days" -> string         (e.g.)
                                                #        "room" -> string         (e.g.)
                                                #        "building" -> string     (e.g.)
                                                #        "classtype" -> string    (e.g.)
                                                #        "start_time" -> string   (e.g.)
                                                #        "end_time" -> string     (e.g.)

                self.open_seats = open_seats      #Number of remaining seats
                self.waitlist = waitlist          #Number of people on the waitlist
                self.instructors = instructors    #Array of professor names for section (e.g.)

#Should be enough for this file, don't need getters cause everything is public.