document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from the server and update the placeholders
    fetch('/api/get_course_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // Provide the subject and class_code based on your requirements
            subject: 'CSE',
            class_code: '260',
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Update course information
        document.getElementById('courseTitle').innerText = `Course Title: ${data.COURSE_TITLE_DESCR}`;

        // Update instructors list
        const instructorsList = document.getElementById('instructorsList');
        instructorsList.innerHTML = '<li>Instructors:</li>';
        data.INSTRUCTORS.forEach(instructor => {
            const li = document.createElement('li');
            li.innerText = instructor;
            instructorsList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching course information:', error));

    // Fetch grade data from the server and update the placeholders
    fetch('/api/get_grade_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // Provide the course_name based on your requirements
            course_name: 'example_course',
        }),
    })
    .then(response => response.json())
    .then(gradeData => {
        // Update grade information
        document.getElementById('averageGrade').innerText = `Average Grade: ${gradeData.AVERAGE_GRADE}`;
        document.getElementById('medianGrade').innerText = `Median Grade: ${gradeData.MEDIAN_GRADE}`;
    })
    .catch(error => console.error('Error fetching grade data:', error));

    // Fetch professor rating from the server and update the placeholders
    fetch('/api/prof_rating/example_professor')
    .then(response => response.json())
    .then(profRating => {
        // Update professor rating information
        document.getElementById('profRating').innerText = `Professor Rating: ${profRating.RATING}`;
        document.getElementById('difficulty').innerText = `Difficulty: ${profRating.DIFFICULTY}`;
    })
    .catch(error => console.error('Error fetching professor rating:', error));
});
