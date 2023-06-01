// Get the CSRF token from the cookie
function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

const csrftoken = getCookie('csrftoken');

// Add event listeners to the buttons
const parseButton = document.getElementById('parse-file-button');
parseButton.addEventListener('click', () => {
    event.preventDefault();
    // Get the selected values
    const visualizatorSelection = document.getElementById('visualizator-selection').value;
    const parserSelection = document.getElementById('parser-selection').value;
    const fileSelection = document.getElementById('file-selection').files[0]; // Assuming you want to upload a single file

    // Check if a visualizer is selected
    if (visualizatorSelection === 'default') {
        alert('Please select a visualizer before parsing the file.');
        return;
    }

    // Check if a parser is selected
    if (parserSelection === 'default') {
        alert('Please select a parser before parsing the file.');
        return;
    }

    // Create a FormData object to send the data
    const formData = new FormData();
    formData.append('visualization', visualizatorSelection);
    formData.append('parser', parserSelection);
    formData.append('file', fileSelection);

    // Send a POST request to the desired URL
    fetch('/parse_and_visualize', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
        .then(response => {
            // Handle the response as needed
            window.location.href = '/parse_and_visualize';
            console.log(response);
        })
        .catch(error => {
            // Handle any errors
            console.error(error);
        });
});

const loadButton = document.getElementById('load-graph-button');
loadButton.addEventListener('click', () => {
    event.preventDefault();
    // Get the selected values
    const visualizatorSelection = document.getElementById('visualizator-selection').value;
    const graphSelection = document.getElementById('graph-selection').value;

    // Check if a visualizer is selected
    if (visualizatorSelection === 'default') {
        alert('Please select a visualizer before loading the graph.');
        return;
    }

    // Check if a graph is selected
    if (graphSelection === 'default') {
        alert('Please select a graph before loading.');
        return;
    }

    // Create a FormData object to send the data
    const formData = new FormData();
    formData.append('visualization', visualizatorSelection);
    formData.append('graph', graphSelection);

    // Send a POST request to the desired URL
    fetch('/load_and_visualize', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
        .then(response => {
            // Handle the response as needed
            window.location.href = '/load_and_visualize';
            console.log(response);
        })
        .catch(error => {
            // Handle any errors
            console.error(error);
        });
});
