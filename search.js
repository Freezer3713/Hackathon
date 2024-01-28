function search() {
    var searchTerm = document.getElementById("searchBar").value;

    // Call the Flask API to get course information
    fetch('/api/get_course_info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            subject: searchTerm,
            class_code: searchTerm,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Navigate to the new results page with the obtained data
        window.location.href = '/results';
    })
    .catch(error => console.error('Error:', error));
}
