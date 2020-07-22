'''
Holds all Section objects for a Schedule
Is a more specific instance of CourseList
'''

import Section

class Schedule:

    def __init__(self):
        self.sections = []      # Array of Section objects
        self.compiled_sections = set() # Hash set containing all day/time tuples for the Schedule

    def __str__(self):
        out = "{"
        for section in self.sections:
            out += section.section_id + ", "
        out = out[:-2]
        out += "}"

        return out

    # Compares new section's tuple set to the rest of the schedule
    # Adds the section and returns true if legal, returns false otherwise
    def add_section(self, section):
        # Stores ordered tuples representing indices for active time slots
        tuple_set = section.get_tuple_set()

        # Compare active_slots to compiled master list
        for pair in tuple_set:
            if pair in self.compiled_sections:
                # The new section overlaps with an existing section
                return False
            
        # New section does not overlap, add it to the schedule and return
        self.sections.append(section)
        
        for pair in tuple_set:
            self.compiled_sections.add(pair)

        return True
    
    def add_sections(self, sections):
        for section in sections:
            self.add_section(section)
    
    def remove_section(self, section):
        tuple_set = section.get_tuple_set()

        for pair in tuple_set:
            self.compiled_sections.remove(pair)

        self.sections.remove(section)
    
    def remove_sections(self, sections):
        for section in sections:
            self.remove_section(section)

    def clear(self):
        self.sections.clear()
        self.compiled_sections.clear()