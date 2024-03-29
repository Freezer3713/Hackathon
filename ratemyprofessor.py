import ratemyprofessor
import requests
from bs4 import BeautifulSoup
def prof_rating(prof_name):
    

    msu = ratemyprofessor.get_school_by_name("Michigan State University")
    professor = ratemyprofessor.get_professor_by_school_and_name(msu, prof_name) 
    print(professor.difficulty)
    print(professor.rating)
    
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
