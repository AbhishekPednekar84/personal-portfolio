const navItemsPortfolio = document.querySelectorAll('.nav-item');
var bodyElem = document.getElementById('bg-img');
var liCurrent = document.querySelector('li:nth-child(2)');

// Remove the background image from the profile page
bodyElem.removeAttribute('id');

// Remove the current class (if present) from all list items
navItemsPortfolio.forEach(itemPortfolio => itemPortfolio.classList.remove('current'));

// Add the current class for the portfolio list item
liCurrent.classList.add('current');



