class GEProgress:
    """This class determines what ge areas are not completed.
    """
    def __init__(self, completed_ge_courses, completed_ge_units, student_id, ge_plan_requirements):
        self.student_id = student_id
        self.completed_ge_units = completed_ge_units
        self.completed_ge_courses = completed_ge_courses
        self.ge_plan_requirements = ge_plan_requirements
        self.missing_ge_courses = []

    def ge_requirements_completed(self):
        print('progress ge plan req', self.ge_plan_requirements)
        for ge_key in self.ge_plan_requirements:
            if ge_key not in self.completed_ge_courses:
                self.missing_ge_courses.append(ge_key)
        return self.missing_ge_courses, self.completed_ge_courses, self.completed_ge_units
