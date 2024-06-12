document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.custom-search-input .form-control');

    searchInput.addEventListener('focus', function() {
        this.style.minWidth = '300px'; // Adjust width on focus
    });

    searchInput.addEventListener('blur', function() {
        this.style.minWidth = '200px'; // Reset width on blur
    });

    searchInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            // Perform search operation here, for example:
            const searchTerm = this.value.trim();
            if (searchTerm !== '') {
                // Redirect to search results page or perform search operation
                console.log('Searching for:', searchTerm);
            }
        }
    });
});
