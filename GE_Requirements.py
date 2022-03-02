import pandas as pd

class GeRequirements:


    def __init__(self, degree_applicable_dict, ge_plan):
        self.degree_applicable_dict = degree_applicable_dict
        self.ge_plan = ge_plan
        self.completed_ge_courses = {}
        self.completed_ge_units = []
        self.ge_course_list = []

    def construct_ge_dataframe(self):
        ge_dataframe = pd.read_csv(self.ge_plan)
        return ge_dataframe

    def ge_courses_completed(self, area_name, ge_dataframe):
        for i in range(len(ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, area_name]:
                    if area_name not in self.completed_ge_courses:
                        if key not in self.ge_course_list:
                            self.completed_ge_courses[area_name] = {'course': key, 'units': self.degree_applicable_dict[key]['units']}
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
                            ge_units_total = sum(d['units'] for d in self.completed_ge_courses.values()if d)
                            self.ge_course_list = [d['course'] for d in self.completed_ge_courses.values() if d]
        return self.completed_ge_courses, self.completed_ge_units


    def ge_requirements_completed(self, ge_plan_list):
        missing_ge_courses = []
        for area in ge_plan_list:
            if area not in self.completed_ge_courses:
                missing_ge_courses.append(area)
        return missing_ge_courses

    def area_e_ge_requirements(self, ge_dataframe):
        area_e_list = []
        print('units', self.completed_ge_units)
        totalGEUnits=sum(item['units'] for item in self.completed_ge_units)
        # total_ge_units = sum(self.completed_ge_units)
        for i in range(len(ge_dataframe['Electives'])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, 'Electives']:
                    if len(self.completed_ge_courses) == 9:
                        if totalGEUnits < 18:
                            area_e_list.append(key)
                            self.completed_ge_courses['AreaE'] = area_e_list
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
        return self.completed_ge_courses

    def reading_proficiency(self):
        print('reading comp ge', self.completed_ge_courses)
        if 'Reading Proficiency' not in self.completed_ge_courses:
            # totalGEUnits = sum(item['units'] for item in self.completed_ge_units)
            if sum(item['units'] for item in self.completed_ge_units) >= 12:
                self.completed_ge_courses['Reading_Proficiency'] = 'Met(GE Units)'
                # print(self.completed_ge_courses)
        return self.completed_ge_courses