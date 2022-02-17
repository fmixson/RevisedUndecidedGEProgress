from easygui import fileopenbox
from Enroll_Hist_DF import EnrollmentHistoryDataFrame
from Student_ID import StudentID
from Course_Info import CourseInfo
from Student_Info import StudentInfo
from GE_Requirements import GeRequirements
from Social_Behavioral_Areas import SocialBehavAreas

def degree_progess(student_id,  enrollment_history_df, ge_plan, ge_plan_list):
    sinfo = StudentInfo(student_id=id, enrollment_history_df=enrollment_history_df)
    degree_applicable_courses = sinfo.completed_courses()
    current_courses = coursInfo.current_courses()
    gereq = GeRequirements(degree_applicable_dict=degree_applicable_courses, ge_plan=ge_plan)
    ge_dataframe = gereq.construct_ge_dataframe()
    # gereq.ge_courses_completed(ge_dataframe=ge_dataframe)
    socbeh = SocialBehavAreas(degree_applicable_dict=degree_applicable_courses, ge_dataframe=ge_dataframe)
    for area in ge_plan_list:
        if area == 'Electives':
            gereq.area_e_ge_requirements()
        if area == 'Reading_Proficiency':
            gereq.reading_proficiency()
        if area == 'Soc_Behav1' or area == 'Soc_Behav2' or area == 'Soc_Behav3':
            socbeh.ge_courses_completed(area_name=area, ge_courses_completed=ge_courses_completed)
        else:
            ge_courses_completed = gereq.ge_courses_completed(area_name=area, ge_dataframe=ge_dataframe)
    missing_ge_courses = gereq.ge_requirements_completed(ge_plan_list)




planAList = ['Math_Proficiency', 'Writing_Proficiency', 'Reading_Proficiency', 'Health_Proficiency', 'Nat_Sci', 'Soc_Sci',
             'Beh_Sci', 'FA_Hum', 'Comp', 'Analytic', 'Electives']
Plan_B_list = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
Plan_B_list_21 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
Plan_C_list = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2', 'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

enrollment_history_file = fileopenbox('Upload Ernollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
studID = StudentID(enrollment_history_df=enrollment_history_df)
studIDList = studID.student_ids()

GePlans = ['PlanA', 'PlanB', 'PlanC']
for plan in GePlans:
    for id in studIDList:
        coursInfo = CourseInfo(student_id=id, enrollment_history_df=enrollment_history_df)
        semester = coursInfo.first_term()
        catalogTerm = coursInfo.calculate_catalog_term()
        if plan == 'PlanA':
            degree_progess(student_id=studID, enrollment_history_df=enrollment_history_df, ge_plan='PlanA_GE.csv',
                           ge_plan_list=planAList)

