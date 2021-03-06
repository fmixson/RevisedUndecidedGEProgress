import pandas as pd

class GeRequirements:
    proficiencies = ['Math_Proficiency', 'Writing_Proficiency', 'Health_Proficiency', 'Reading Proficiency',
                     'Phys_Sci',
                     'Bio_Sci']

    def __init__(self, degree_applicable_dict, ge_plan):
        self.degree_applicable_dict = degree_applicable_dict
        self.ge_plan = ge_plan
        self.completed_ge_courses = {}
        self.completed_ge_units = []
        self.ge_course_list = []

    def construct_ge_dataframe(self):
        ge_dataframe = pd.read_csv(self.ge_plan)
        return ge_dataframe

    def _sciLabs(self, area_name, ge_dataframe):
        for i in range(len(ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, area_name]:
                    self.completed_ge_courses[area_name] = {'course': key,
                                                            'units': self.degree_applicable_dict[key]['units']}
        return self.completed_ge_courses


    def ge_courses_completed(self, area_name, ge_dataframe):
        # # proficiencies = ['Math_Proficiency', 'Writing_Proficiency', 'Health_Proficiency', 'Reading Proficiency',
        #                  'Phys_Sci',
        #                  'Bio_Sci']

        for i in range(len(ge_dataframe[area_name])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, area_name]:
                    if area_name not in self.completed_ge_courses:
                        if area_name == 'Sci_Lab':
                            GeRequirements._sciLabs(area_name=area_name, ge_dataframe=ge_dataframe)

                        if key not in self.ge_course_list:
                            self.completed_ge_courses[area_name] = {'course': key, 'units': self.degree_applicable_dict[key]['units']}
                            if area_name not in GeRequirements.proficiencies:
                                self.completed_ge_units.append(self.degree_applicable_dict[key])
                            ge_units_total = sum(d['units'] for d in self.completed_ge_courses.values()if d)
                            # if area_name not in proficiencies:
                            #     self.ge_course_list.append(key)
                            self.ge_course_list = [self.completed_ge_courses[x]['course'] for x in self.completed_ge_courses
                                                   if x not in GeRequirements.proficiencies]
        print(self.completed_ge_courses)
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
        totalGEUnitsTest=sum(self.completed_ge_courses[x]['units'] for x in self.completed_ge_courses if x
                             not in GeRequirements.proficiencies)
        print(totalGEUnitsTest, totalGEUnits)
        # total_ge_units = sum(self.completed_ge_units)
        for i in range(len(ge_dataframe['Electives'])):
            for key in self.degree_applicable_dict:
                if key == ge_dataframe.loc[i, 'Electives']:
                    if len(self.completed_ge_courses) == 9:
                        print('len of ge', len(self.completed_ge_courses))
                        print('total units', totalGEUnits)
                        if totalGEUnits < 18:
                            print('below if total', totalGEUnits)
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