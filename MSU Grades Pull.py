import pandas as pd

file_path = 'MSU_Grades.csv'
df = pd.read_csv(file_path)


def get_course_info(subject, class_code):
    # Filter the DataFrame based on the given parameters
    course_info = df[(df['SUBJECT'] == subject) & (df['CRSE_CODE'] == class_code)]

    # Check if there are any rows matching the criteria
    if course_info.empty:
        return "No information available for the specified class."

    # Filter out non-numeric grades
    numeric_grades = pd.to_numeric(course_info['GRADE'], errors='coerce')

    # Calculate the average grade for all sections
    average_grade = numeric_grades.mean()

    # Get other relevant information (course title and instructors)
    course_title = course_info['COURSE_TITLE_DESCR'].iloc[0]  # Assuming it's the same for all sections
    instructors = course_info['INSTRUCTOR'].unique()

    # Return the information
    return {
        'COURSE_TITLE_DESCR': course_title,
        'INSTRUCTORS': instructors,
        'AVERAGE_GRADE': average_grade
    }

    # Example usage
subject = 'CSE'
class_code = '102'

course_info = get_course_info(subject, class_code)
print(course_info)