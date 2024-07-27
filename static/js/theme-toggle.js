document.addEventListener('DOMContentLoaded', function() {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    console.log("Current Theme at Load:", currentTheme);
    document.documentElement.setAttribute('data-theme', currentTheme);

    themeToggleBtn.addEventListener('click', function() {
        let theme = document.documentElement.getAttribute('data-theme');
        console.log("Current Theme Before Toggle:", theme);
        if (theme === 'dark') {
            theme = 'light';
            themeToggleBtn.innerHTML = '<i class="fas fa-lightbulb"></i>';
            console.log("Theme set to light");
        } else {
            theme = 'dark';
            themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
            console.log("Theme set to dark");
        }
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        console.log("Theme stored in localStorage:", theme);
    });
});
