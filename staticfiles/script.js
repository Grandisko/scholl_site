// script.js

// Add event listener to navigation links
document.querySelectorAll('header nav a').forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const target = event.target.getAttribute('href');
    document.querySelector(target).scrollIntoView({ behavior: 'smooth' });
  });
});