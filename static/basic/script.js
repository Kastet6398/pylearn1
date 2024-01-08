
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    var htmlElement = document.querySelector('html');
    htmlElement.setAttribute('data-bs-theme', 'dark');
}
