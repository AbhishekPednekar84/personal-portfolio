const navItemsBlog = document.querySelectorAll('.nav-item');
var bodyElem = document.getElementById('bg-img');
var liCurrent = document.querySelector('li:nth-child(3)');

// Remove the background image from the profile page
bodyElem.removeAttribute('id');

// Remove the current class (if present) from all list items
navItemsBlog.forEach(itemBlog => itemBlog.classList.remove('current'));

// Add the current class for the portfolio list item
liCurrent.classList.add('current');

$(document).ready(function () {

    // This hack is needed since the list of blogs is being generated via for loop
    $("li").each(function (index) {
        var index = index + 1; // increment the index since it starts at 0
        var list = "li.blog" + index; // append the index to the class name since                                         they are generated fynamically in jinja2 
        var box = "#box" + index;
        $(box).hide();
        $(box).addClass("blog-description");

        $(list).click(function () {
            $(box).slideToggle()
        })
    })
})
