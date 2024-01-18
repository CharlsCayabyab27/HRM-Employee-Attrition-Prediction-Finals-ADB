const applyTheme = (theme) => {
  document.body.removeAttribute('class');
  document.body.classList.add(theme);
  localStorage.setItem('theme', theme);
};

const toggleTheme = () => {
  const themes = ['dark-mode', 'peach-mode', 'dark-green-mode'];
  const currentTheme = localStorage.getItem('theme');
  const currentIndex = themes.indexOf(currentTheme);

  const nextIndex = (currentIndex + 1) % themes.length;
  const nextTheme = themes[nextIndex];

  applyTheme(nextTheme);
};

const themeToggleBtns = document.querySelectorAll('#theme-toggle');

// Apply stored theme
const theme = localStorage.getItem('theme');
theme && applyTheme(theme);

// Events
themeToggleBtns.forEach(btn => btn.addEventListener('click', toggleTheme));

// Optional: Set initial theme if not stored
if (!theme) {
  applyTheme('dark-mode'); // You can set the initial theme to dark mode, peach mode, or dark green mode
}
