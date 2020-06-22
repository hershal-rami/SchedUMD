'''
Class to house data on all sections of a course

i.e. all CMSC351 sections
'''

class Course:

    def __init__(self, course_id, sections, semester, credits,
        dept_id, grading_method, core, gen_ed, relationships):
                self.course_id = course_id              # The associated course id (ENGL101)
                self.sections = sections                # List of Section objects for the course (0101, 0102, 0201, etc.)
                self.semester = semester                # Numeric representation YYYYMM (202001)
                self.credits = credits                  # Number of credits for the course (2, 3, 4, etc.)
                self.dept_id = dept_id                  # 4 letter department code, useful for narrowing down search (CMSC, MATH, etc.)
                self.grading_method = grading_method    # Can be used to narrow down search as well
                self.core = core                        # Core requirements that this course fulfills
                self.gen_ed = gen_ed                    # Gen ed requirements that this course fulfills
                self.relationships = relationships      # Dictionary that holds information on coreqs, prereqs, cross-listings, etc.

#Should be enough for this file, don't need getters cause everything is public.