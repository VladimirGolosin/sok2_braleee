function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

const csrftoken = getCookie('csrftoken');


const parseButton = document.getElementById('parse-file-button');
parseButton.addEventListener('click', () => {
    event.preventDefault();
    const visualizatorSelection = document.getElementById('visualizator-selection').value;
    const parserSelection = document.getElementById('parser-selection').value;
    const fileSelection = document.getElementById('file-selection').files[0];

    if (visualizatorSelection === 'default') {
        alert('Please select a visualizer before parsing the file.');
        return;
    }

    if (parserSelection === 'default') {
        alert('Please select a parser before parsing the file.');
        return;
    }

    const formData = new FormData();
    formData.append('visualization', visualizatorSelection);
    formData.append('parser', parserSelection);
    formData.append('file', fileSelection);

    fetch('/parse_and_visualize', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
        .then(response => {
            window.location.href = '/parse_and_visualize';
            console.log(response);
        })
        .catch(error => {
            console.error(error);
        });
});

const loadButton = document.getElementById('load-graph-button');
loadButton.addEventListener('click', () => {
    event.preventDefault();
    const visualizatorSelection = document.getElementById('visualizator-selection').value;
    const graphSelection = document.getElementById('graph-selection').value;

    if (visualizatorSelection === 'default') {
        alert('Please select a visualizer before loading the graph.');
        return;
    }

    if (graphSelection === 'default') {
        alert('Please select a graph before loading.');
        return;
    }

    const formData = new FormData();
    formData.append('visualization', visualizatorSelection);
    formData.append('graph', graphSelection);

    fetch('/load_and_visualize', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
        .then(response => {
            window.location.href = '/load_and_visualize';
            console.log(response);
        })
        .catch(error => {
            console.error(error);
        });
});
