'''
Holds all Section objects for a Schedule
Is a more specific instance of CourseList
'''

import Section

class Schedule:

    def __init__(self):
        self.sections = []      # Array of Section objects

    def __str__(self):
        out = "{"
        for section in self.sections:
            out += section.course_id + ", "
        out = out[:-2]
        out += "}"

        return out

    def add_section(self, section):
        self.sections.append(Section.Section(section))
    
    def add_sections(self, sections):
        for section in sections:
            self.add_section(section)
    
    def remove_section(self, section):
        self.sections.remove(section)
    
    def remove_sections(self, sections):
        for section in sections:
            self.remove_section(section)

    # Can add other functions to manipulate array later