from easygui import fileopenbox
from Enroll_Hist_DF import EnrollmentHistoryDataFrame
from Student_ID import StudentID
from Course_Info import CourseInfo
from Student_Info import StudentInfo
from GE_Requirements import GeRequirements
from Social_Behavioral_Areas import SocialBehavAreas
from GE_Progress import GEProgress
from GE_Courses_Report import GECompletionReport

def degree_progess(student_id, enrollment_history_df, ge_plan, ge_plan_list):
    planARequirements = {'Math_Proficiency': 0, 'Writing_Proficiency': 0, 'Reading_Proficiency': 0,'Health_Proficiency': 0,
                         'Nat_Sci': 0,'Soc_Sci': 0, 'FA_Hum': 0, 'Comp': 0, 'Analytic': 0}
    planBGeRequirements = {'Oral_Comm': 0, 'Writ_Comm': 0, 'Crit_Think': 0, 'Phys_Sci': 0, 'Bio_Sci': 0, 'Sci_Labs': 0,
                           'Math': 0, 'Arts': 0, 'Hum': 0, 'Arts_Hum': 0, 'Amer_Hist': 0, 'Amer_Gov': 0,'Institutions': 0,
                           'Self_Dev': 0}
    planB21GeRequirements = {'Oral_Comm': 0, 'Writ_Comm': 0, 'Crit_Think': 0, 'Phys_Sci': 0, 'Bio_Sci': 0, 'Sci_Labs': 0,
                             'Math': 0, 'Arts': 0, 'Hum': 0, 'Arts_Hum': 0, 'Amer_Hist': 0, 'Amer_Gov': 0,'Institutions': 0,
                             'Self_Dev': 0}
    eligibleCoursesDF=e.eligible_courses_df()
    sinfo = StudentInfo(student_id, enrollment_history_df=eligibleCoursesDF)
    degree_applicable_courses = sinfo.completed_courses()
    enrolled_courses = coursInfo.current_courses()
    gereq = GeRequirements(degree_applicable_dict=degree_applicable_courses, ge_plan=ge_plan)
    ge_dataframe = gereq.construct_ge_dataframe()
    # gereq.ge_courses_completed(ge_dataframe=ge_dataframe)
    socbeh = SocialBehavAreas(degree_applicable_dict=degree_applicable_courses, ge_dataframe=ge_dataframe)
    print('area', ge_plan_list)
    for area in ge_plan_list:
        print('area', area)
        if area == 'Electives':
            gereq.area_e_ge_requirements(ge_dataframe)
        if area == 'Reading_Proficiency':
            gereq.reading_proficiency()
        if area == 'Soc_Behav1' or area == 'Soc_Behav2' or area == 'Soc_Behav3':
            socbeh.ge_courses_completed(area_name=area, ge_courses_completed=geCoursesCompleted)
        else:
            geCoursesCompleted, ge_units_completed = gereq.ge_courses_completed(area_name=area, ge_dataframe=ge_dataframe)
    missing_ge_courses = gereq.ge_requirements_completed(ge_plan_list)
    geProgress = GEProgress(completed_ge_courses=geCoursesCompleted, completed_ge_units=ge_units_completed, student_id=id,
                            ge_plan_requirements=planARequirements)
    missing_ge_courses, geCoursesCompleted, ge_units_completed = geProgress.ge_requirements_completed()
    print('missing', missing_ge_courses, 'completed', geCoursesCompleted, 'units', ge_units_completed)
    ge_report = GECompletionReport(student_id,
                                   completed_ge_courses=geCoursesCompleted,
                                   missing_ge_courses=missing_ge_courses,
                                   completed_ge_units=ge_units_completed,
                                   plan=plan,
                                   current_enrollment=enrolled_courses,
                                   first_term=semester,
                                   # all_count=all_courses,
                                   passed_courses=degree_applicable_courses)
    ge_report.ge_completion()


planAList = ['Math_Proficiency', 'Writing_Proficiency', 'Reading_Proficiency', 'Health_Proficiency', 'Nat_Sci', 'Soc_Sci',
             'Beh_Sci', 'FA_Hum', 'Comp', 'Analytic', 'Electives']
planBList = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist', 'Amer_Gov', 'Institutions', 'Self_Dev']
planBList21 = ['Oral_Comm', 'Writ_Comm', 'Crit_Think', 'Phys_Sci', 'Bio_Sci', 'Sci_Labs', 'Math', 'Arts', 'Hum', 'Arts_Hum',
               'Amer_Hist_Gov', 'Institutions', 'Self_Dev', 'Ethnic_Stds']
PlanCList = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum', 'Soc_Behav1', 'Soc_Behav2', 'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']

enrollment_history_file = fileopenbox('Upload Ernollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
# eligibleCoursesDF = e.eligible_courses_df()
studID = StudentID(enrollment_history_df=enrollment_history_df)
studIDList = studID.student_ids()

GePlans = ['PlanA', 'PlanB', 'PlanC']
for plan in GePlans:
    for id in studIDList:
        coursInfo = CourseInfo(student_id=id, enrollment_history_df=enrollment_history_df)
        semester = coursInfo.first_term()
        catalogTerm = coursInfo.calculate_catalog_term()
        print('plan', plan)
        if plan == 'PlanA':
            degree_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanA_GE.csv',
                           ge_plan_list=planAList)
        if plan == 'PlanB':
            if catalogTerm >= 1219:
                degree_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanB_GE_2021.csv',
                                ge_plan_list=planBList21)
            else:
                degree_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanB_GE.csv',
                                ge_plan_list=planBList)
        if plan == 'PlanC':
            degree_progess(student_id=id, enrollment_history_df=enrollment_history_df, ge_plan='PlanC_GE.csv', ge_plan_list=PlanCList)
GECompletionReport.GE_Progress_df.to_csv('C:/Users/fmixson/Desktop/Undecided_GE_Draft.csv')
