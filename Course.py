'''
Class to house all data on a course

i.e. Credits, semester, department, etc. for CMSC132
'''

import time
import requests
import Section
from urllib3.exceptions import InsecureRequestWarning

class Course:

    def __init__(self, course_id):
        
        # Supress the certificate verification warning
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        t0 = time.time()
        # Gets API data without certificate verification
        r = requests.get('https://api.umd.io/v1/courses/' + course_id, verify=False).json()[0]
        
        #out += query_by_Id(course).json()[0].get("course_id"))

        self.course_id = course_id    # The associated course id (ENGL101)
        self.sections = []
        
        # Concatenates all sections into one string to reduce number of API calls
        sectionStrings = r.get("sections")
        appStr = ""
        for section in sectionStrings:
            appStr += section + ","

        appStr = appStr[:-1]
        secr = requests.get('https://api.umd.io/v1/courses/sections/' + appStr, verify=False).json()

        t1 = time.time()
        print("Request for " + course_id + " took: " + str(t1-t0)[:5])
        for section in secr:
            self.sections.append(Section.Section(section))
        
        #self.sections = r.get("sections")                # List of Section objects for the course (0101, 0102, 0201, etc.)
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
        out += "----credits----\n"
        out += self.credits
        out += "\n----dept_id----\n"
        out += self.dept_id
        out += "\n----grading_method----\n"
        for method in self.grading_method:
            out += str(method) + "\n"
        out += "----core----\n"
        for core in self.core:
            out += str(core) + "\n"
        out += "----gen_ed----\n"
        for gen_ed in self.gen_ed:
            out += str(gen_ed) + "\n"
        out += "----relationships----\n"
        for relationship in self.relationships:
            out += str(relationship) + "\n"
        out += "----sections----\n"
        for section in self.sections:
            out += str(section) + "\n"
        return out

    def get_section_data(self, section_number):
        for section in self.sections:
            if section.section_id == section_number or section.number == section_number:
                return str(section)
                break
        return 'Section not found.'
        
#Should be enough for this file, don't need getters cause everything is public.
