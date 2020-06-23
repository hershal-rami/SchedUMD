'''
Class to house data on all sections of a course

i.e. all CMSC351 sections
'''

import requests
import Section

class Course:

    def __init__(self, course_id):
            
        r = requests.get('https://api.umd.io/v1/courses/' + course_id).json()[0]
        
        #out += query_by_Id(course).json()[0].get("course_id"))

<<<<<<< HEAD
        self.course_id = course_id                       # The associated course id (ENGL101)
=======
        self.course_id = course_id              # The associated course id (ENGL101)

        self.sections = []
        
        sectionStrings = r.get("sections")
        for section in sectionStrings:
            self.sections.append(Section.Section(section))
        
>>>>>>> 182e3f49f3a9cd2156a3e0ee3722fe5cd9f1fd7c
        self.sections = r.get("sections")                # List of Section objects for the course (0101, 0102, 0201, etc.)
        self.semester = r.get("semester")                # Numeric representation YYYYMM (202001)
        self.credits = r.get("credits")                  # Number of credits for the course (2, 3, 4, etc.)
        self.dept_id = r.get("dept_id")                  # 4 letter department code, useful for narrowing down search (CMSC, MATH, etc.)
        self.grading_method = r.get("grading_method")    # Can be used to narrow down search as well
        self.core = r.get("core")                        # Core requirements that this course fulfills
        self.gen_ed = r.get("gen_ed")                    # Gen ed requirements that this course fulfills
        self.relationships = r.get("relationships")      # Dictionary that holds information on coreqs, prereqs, cross-listings, etc.

    def __str__(self):
        out = "" 

        out += "====" + self.course_id + "====\n"
        out += "\n----sections----\n"
        for section in self.sections:
            out += str(section) + "\n"
        out += "----credits----\n"
        out += self.credits
        out += "\n----dept_id----\n"
        out += self.dept_id
        out += "\n----grading_method----\n"
        for method in self.grading_method:
            out += str(section) + "\n"
        out += "----core----\n"
        for core in self.core:
            out += str(core) + "\n"
        out += "----gen_ed----\n"
        for gen_ed in self.gen_ed:
            out += str(gen_ed) + "\n"
        out += "----relationships----\n"
        for relationship in self.relationships:
            out += str(relationship) + "\n"

        return out


        
#Should be enough for this file, don't need getters cause everything is public.
