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


// stelute pentru buton


    $(document).ready(function() {
    // Function to trigger stars animation on a specific button
    function showStarsAnimation($element) {
        var offset = $element.offset();
        var $stars = $('<div class="stars">✨✨✨</div>');

        $stars.css({
            position: 'absolute',
            top: offset.top - $element.height(),
            left: offset.left,
            fontSize: '20px',
            color: 'gold',
            zIndex: 1000,
            pointerEvents: 'none'
        });

        $('body').append($stars);

        $stars.animate({
            top: '-=50',
            opacity: 0
        }, 1000, function () {
            $(this).remove();
        });
    }

    // Handle add to cart form submission
    $('form.add-to-cart').on('submit', function(event) {
    event.preventDefault();

    var $form = $(this);
    var url = $form.attr('action');
    var formData = $form.serialize();
    var $submitButton = $form.find('button[type="submit"]');

    $.post(url, formData, function(data) {
    if (data.status === 'success') {
    showStarsAnimation($submitButton);
    if (data.button === 'cart') {
    showStarsAnimation($('.view-cart'));
}
} else {
    alert('An error occurred while adding the product to the cart.');
}
});
});

    // Handle add to favorites form submission
    $('form.add-to-favorites').on('submit', function(event) {
    event.preventDefault();

    var $form = $(this);
    var url = $form.attr('action');
    var formData = $form.serialize();
    var $submitButton = $form.find('button[type="submit"]');

    $.post(url, formData, function(data) {
    if (data.status === 'success') {
    showStarsAnimation($submitButton);
    if (data.button === 'favorites') {
    showStarsAnimation($('.view-favorites'));
}
} else {
    alert('An error occurred while adding the product to the favorites.');
}
});
});

    // Optional: Handle AJAX-based add to cart/favorites links
    $('.add-to-cart-link').on('click', function(event) {
    event.preventDefault();

    var $link = $(this);
    var url = $link.attr('href');

    $.get(url, function(data) {
    if (data.status === 'success') {
    showStarsAnimation($link);
} else {
    alert('An error occurred while adding the product.');
}
});
});

    $('.add-to-favorites-link').on('click', function(event) {
    event.preventDefault();

    var $link = $(this);
    var url = $link.attr('href');

    $.get(url, function(data) {
    if (data.status === 'success') {
    showStarsAnimation($link);
} else {
    alert('An error occurred while adding the product.');
}
});
});
});





