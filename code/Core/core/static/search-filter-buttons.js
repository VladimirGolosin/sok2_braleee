const searchButton = document.getElementById('search-button');
    searchButton.addEventListener('click', () => {
        event.preventDefault();
        // Get the search filter text
        const searchFilterText = document.getElementById('search-filter-input').value;

        // Check if the search filter text is empty
        if (searchFilterText.trim() === '') {
            alert('Please enter a search filter text.');
            return;
        }

        // Redirect to the search URL with the search filter text as a parameter
        window.location.href = `/search/${encodeURIComponent(searchFilterText)}`;
    });


    const filterButton = document.getElementById('filter-button');
    filterButton.addEventListener('click', () => {
        event.preventDefault();
        // Get the filter text
        const filterText = document.getElementById('search-filter-input').value;

        // Check if the filter text is empty
        if (filterText.trim() === '') {
            alert('Please enter a filter text.');
            return;
        }

        // Redirect to the filter URL with the filter text as a parameter
        window.location.href = `/filter/${encodeURIComponent(filterText)}`;
    });