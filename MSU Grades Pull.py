import pandas as pd

file_path = '/Users/afnanrahman/Hackathon/MSU_Grades.csv'
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

def print_course_info(course_info):
    if isinstance(course_info, str):
        print(course_info)
    else:
        print(f"Course Title: {course_info['COURSE_TITLE_DESCR']}")
        print("Instructors:")
        for instructor in course_info['INSTRUCTORS']:
            print(f"  - {instructor}")
        print(f"Average Grade: {course_info['AVERAGE_GRADE']}")

# Example usage
subject = 'CSE'
class_code = '260'

course_info = get_course_info(subject, class_code)
print_course_info(course_info)
