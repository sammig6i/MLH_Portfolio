document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.nav-link');

  // Function to handle the active state
  function setActiveLink() {
      const currentLocation = window.location.pathname;
      links.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === currentLocation) {
              link.classList.add('active');
          }
      });
  }

  setActiveLink();

  links.forEach(link => {
      link.addEventListener('click', function() {
          links.forEach(l => l.classList.remove('active'));
          this.classList.add('active');
      });
  });
});


const menuToggle = document.getElementById('mobile-menu');
const dropdownMenu = document.getElementById('dropdown-menu');

menuToggle.addEventListener('click', () => {
  dropdownMenu.classList.toggle('active');
});

  
  