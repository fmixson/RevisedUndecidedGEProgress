import pandas as pd


class EnrollmentHistoryDataFrame:

    def __init__(self, enrollment_history_file):
        self.enrollment_history_file = enrollment_history_file


    def create_dataframe(self):
        pd.set_option('display.max_columns', None)
        self.enrollment_history_df = pd.read_csv(self.enrollment_history_file, encoding='Latin')
        self.enrollment_history_df.replace(to_replace="SPCH",
                                   value="COMM", inplace=True)
        self.enrollment_history_df.sort_values(['ID'], inplace=True)
        self.enrollment_history_df['Class Subject'] = self.enrollment_history_df['Class Subject'].str.strip()
        self.enrollment_history_df['Class Catalog Number'] = self.enrollment_history_df['Class Catalog Number'].str.strip()
        self.enrollment_history_df['Course'] = self.enrollment_history_df['Class Subject'] + " " + self.enrollment_history_df['Class Catalog Number']
        self.enrollment_history_df['Class Catalog Number'] = self.enrollment_history_df['Class Catalog Number'].fillna(0)
        self.enrollment_history_df['Enrollment Drop Date'] = self.enrollment_history_df['Enrollment Drop Date'].fillna(0)
        # nona_enrollment_history_df = self.enrollment_history_df[self.enrollment_history_df['Class Subject'].notna()]
        # nona_enrollment_history_df = nona_enrollment_history_df.reset_index(drop=True)
        # self.enrollment_history_df = nona_enrollment_history_df
        return self.enrollment_history_df

    def eligible_courses_df(self):
        ineligibleCourses =[]
        ineligible_courses = ['MATH 80A', 'MATH 60', 'ENGL 72', 'ENGL 52', 'ACLR 90', 'ACLR 91', 'ACLR 92', 'CHEM 95A',
                              'CHEM 95B', 'CHEM 95C', 'CHEM 95D', 'CHEM 95E', 'CHEM 95F', 'LIBR 50', 'LAW 98', 'LAW 99',
                              'BCOT 5A']
        no_AED = self.enrollment_history_df['Class Subject'] != "AED"
        no_AED_DF = self.enrollment_history_df[no_AED]
        resetNoAED = no_AED_DF.reset_index(drop=True)
        for i in range(len(resetNoAED)-1):
            if resetNoAED.loc[i, 'Course'] in ineligible_courses:
                ineligibleCourses.append(i)
        eligibleCourses = resetNoAED.drop(ineligibleCourses)
        eligibleCoursesDF = eligibleCourses.reset_index(drop=True)
        return eligibleCoursesDF