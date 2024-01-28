function uploadAndSearch() {
    var fileInput = document.getElementById('csvFile');
    var searchTerm = document.getElementById("searchBar").value;
    var reader = new FileReader();

    reader.onload = function(e) {
        console.log("File content type:", typeof e.target.result); // Debugging: Check file content type
        var text = e.target.result;
        console.log("Search term type:", typeof searchTerm); // Debugging: Check search term type
        var foundLines = findStringInCSV(text, searchTerm);

        // Process or display foundLines here
        console.log("Found lines:", foundLines);
    };

    reader.onerror = function(e) {
        console.error("Error reading file:", e);
    };

    if (fileInput.files.length > 0) {
        reader.readAsText(fileInput.files[0]);
    } else {
        alert('Please select a CSV file to upload.');
    }
}

function findStringInCSV(csvContent, searchString) {
    if (typeof csvContent !== 'string' || typeof searchString !== 'string') {
        console.error('Invalid input: csvContent and searchString should be strings');
        return [];
    }

    const normalizedSearchString = searchString.trim().toLowerCase();
    const lines = csvContent.split(/\r\n|\n|\r/);
    let foundLines = [];

    for (let line of lines) {
        if (typeof line === 'string' && line.trim().toLowerCase().includes(normalizedSearchString)) {
            foundLines.push(line);
        }
    }

    return foundLines;
}
