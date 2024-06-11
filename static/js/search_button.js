document.getElementById('searchButton').onclick = function() {
    var query = document.getElementById('searchQuery').value;
    var url = searchUrl + "?q=" + encodeURIComponent(query);
    window.location.href = url;
}
