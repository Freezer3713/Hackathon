import pandas as pd
import requests
from bs4 import BeautifulSoup

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

# Create a function to validate the course name entered by the user


def main():
    x = get_grade_data('CSE_102')
    print(x.text.strip())
    
main()



    
    



