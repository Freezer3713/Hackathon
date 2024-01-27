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
    course_title = course_info['COURSE_TITLE_DESCR'].iloc[0]  
    instructors_str = course_info['INSTRUCTOR'].iloc[0]  

    # Split instructors into a list if there are multiple instructors
    instructors = [instructor.strip() for instructor in instructors_str.split('|')]

    # Return the information
    return {
        'COURSE_TITLE_DESCR': course_title,
        'INSTRUCTORS': instructors,
    }

def print_course_info(course_info):
    if isinstance(course_info, str):
        print(course_info)
    else:
        print(f"Course Title: {course_info['COURSE_TITLE_DESCR']}")
        print("Instructors:")
        for instructor in course_info['INSTRUCTORS']:
            print(f"  - {instructor}")
        

# Example usage
subject = 'CSE'
class_code = '260'

course_info = get_course_info(subject, class_code)
course_title = course_info['COURSE_TITLE_DESCR']
instructors = course_info['INSTRUCTORS']

# Now you can refer to the instructor names using the 'instructors' list
print(f"Course Title: {course_title}")
print("Instructors:")
for instructor in instructors:
    print(f"  - {instructor}")

