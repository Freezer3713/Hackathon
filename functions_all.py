import ratemyprofessor
import requests
from bs4 import BeautifulSoup
import pandas as pd

def prof_rating(prof_name):
    
    prof_name = prof_name.split(',')
    prof_name = prof_name[0]
    msu = ratemyprofessor.get_school_by_name("Michigan State University")
    professor = ratemyprofessor.get_professor_by_school_and_name(msu, prof_name) 

    
    if professor is not None:
        print("%s works in the %s Department of %s." % (professor, professor.department, professor.school.name))
        print("Rating: %s / 5.0" % professor.rating)
        print("Difficulty: %s / 5.0" % professor.difficulty)
        print("Total Ratings: %s" % professor.num_ratings)
        if professor.would_take_again is not None:
            print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
        else:
            print("Would Take Again: N/A")


def get_grade_data(course_name):
    
    # Get specific URL for specifc course
    url = f'https://msugrades.com/courses/{course_name}/instructors'
    
    # Send HTTP request to the URL
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(id="grade-summary")
    grade = results.find('p')
    return grade



def get_course_info(subject, class_code):
    file_path = '/Users/jordansebagh/Downloads/Hackathon/msu_grades.csv'
    df = pd.read_csv(file_path)
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

        
        
def main():
    
    # Example usage
    subject = 'CSE'
    class_code = '260'

    course_info = get_course_info(subject, class_code)
    course_title = course_info['COURSE_TITLE_DESCR']
    instructors = course_info['INSTRUCTORS']


    # Now you can refer to the instructor names using the 'instructors' variable
    print(f"Course Title: {course_title}")
    print("Instructors:")
    for instructor in instructors:
        print(f"  - {instructor}")
        prof_rating(instructor)
        


main()
