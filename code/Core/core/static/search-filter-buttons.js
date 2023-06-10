const searchButton = document.getElementById('search-button');
searchButton.addEventListener('click', () => {
    event.preventDefault();
    const searchFilterText = document.getElementById('search-filter-input').value;

    if (searchFilterText.trim() === '') {
        alert('Please enter a search filter text.');
        return;
    }

    window.location.href = `/search/${encodeURIComponent(searchFilterText)}`;
});


const filterButton = document.getElementById('filter-button');
filterButton.addEventListener('click', () => {
    event.preventDefault();
    const filterText = document.getElementById('search-filter-input').value;

    if (filterText.trim() === '') {
        alert('Please enter a filter text.');
        return;
    }

    window.location.href = `/filter/${encodeURIComponent(filterText)}`;
});