document.addEventListener('DOMContentLoaded', function () {
    console.log("READY")
    const searchInput = document.getElementById('searchQuery');

    searchInput.addEventListener('focus', function () {
        searchInput.style.backgroundColor = 'aqua';
    });

    searchInput.addEventListener('blur', function () {
        searchInput.style.minWidth = '200px'; // Reset width on blur
    });

    searchInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            // Perform search operation here, for example:
            const searchTerm = searchInput.value.trim();
            if (searchTerm !== '') {
                window.location.href = window.location.origin + '/search/' + encodeURIComponent(searchTerm);
            }
        }
    });

    const forms = document.querySelectorAll('.update-quantity-form');
    forms.forEach((form) => {
        form.querySelector('input[name="quantity"]').addEventListener('change', () => {
            form.submit();
        });
    });
});

document.getElementById('searchButton').onclick = function () {

    let query = document.getElementById('searchQuery').value;
    if (query !== '') {
    const url = window.location.origin + '/search/' + query;
    window.location.replace(url);
    } else {
        // Nu facem nimic dacă termenul de căutare este gol
    }
}

// Add hover effect
const cartItems = document.querySelectorAll('.cart-item');
cartItems.forEach((item) => {
    item.addEventListener('mouseover', () => {
        item.style.transform = 'scale(1.05)';
    });
    item.addEventListener('mouseout', () => {
        item.style.transform = 'scale(1)';
    });
});




