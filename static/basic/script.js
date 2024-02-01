const htmlElement = document.querySelector('html');
const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

function handleColorSchemeChange(e) {
  if (e.matches) {
    htmlElement.setAttribute('data-bs-theme', 'dark');
  } else {
    htmlElement.setAttribute('data-bs-theme', 'light');
  }
}

handleColorSchemeChange(mediaQuery);
mediaQuery.addEventListener('change', handleColorSchemeChange);
