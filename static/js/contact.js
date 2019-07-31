const navItemsContact = document.querySelectorAll('.nav-item');
var bodyElem = document.getElementById('bg-img');
var liCurrent = document.querySelector('li:nth-child(4)');

// Remove the background image from the profile page
bodyElem.removeAttribute('id');

// Remove the current class (if present) from all list items
navItemsContact.forEach(itemContact => itemContact.classList.remove('current'));

// Add the current class for the portfolio list item
liCurrent.classList.add('current');



