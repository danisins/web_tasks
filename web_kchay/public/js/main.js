/*nav-toggle*/
let nav = document.getElementById('nav_toggle');
let menu = document.getElementById('header__inner-active');
let person = document.getElementById('head_person');



nav.addEventListener('click', function(){
    nav.classList.toggle('active');
    menu.classList.toggle('active');
    person.classList.toggle('active');
})
/* /nav-toggle*/


