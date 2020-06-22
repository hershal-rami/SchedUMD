'''
Class to house all data for a section of a Course

i.e. The location, time, professor, etc. for CMSC132-0101
'''

class Section:

    def __init__(self, ):
                self.number = number              # Second half of sectionID (0101)
                self.instructors = instructors    # Array of professor names for section (e.g.)
                self.seats = seats                # Total number of seats for section
                self.open_seats = open_seats      # Number of remaining seats
                self.waitlist = waitlist          # Number of people on the waitlist
                
                self.meetings = meetings          # Dictionary housing meeting info for the section
                '''   
                                                dictionary defined as follows
                                                First element in the list represents lecture, second represents discussions
                                                (if there are no discussions then the list will be of size 1)
                                                        "days" -> list         (e.g.) [MWF, MW]
                                                        "room" -> list         (e.g.) [0324, 2118]
                                                        "building" -> list     (e.g.) [IRB, CSI]
                                                        "classtype" -> list    (e.g.) [Lecture, Discussion]
                                                        "start_time" -> list   (e.g.) [3:00pm, 12:00pm]
                                                        "end_time" -> list     (e.g.) [3:50pm, 12:50pm]
                '''
