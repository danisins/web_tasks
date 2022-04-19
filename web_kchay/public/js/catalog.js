/*fiter*/
let filter = document.getElementById('filter__title');
let filter__main = document.getElementById('filter__main');

filter.addEventListener('click', function(){
    filter__main.classList.toggle('active');
})
/* /fiter*/

/*orientation*/
let list = document.getElementById('list');
let grid = document.getElementById('grid');
let katalog = document.getElementById('katalog');

grid.addEventListener('click', function(){
    katalog.classList.toggle('active');
})
/*/orientation*/

/*document.getElementById('grid').onclick = function() {

  document.querySelector('.katalog__nomber').classList.toggle('active');
}*/


/*let i = ocument.querySelector('.katalog__nomber')
 
for (i = 0; i < Things.length; i++) {
	Things[i]
}
*/


/*document.getElementById('grid').addEventListener('click', () => {
  document.querySelectorAll('.katalog__nomber').classList.toggle('active');
});*/


document.getElementById('grid').addEventListener('click', () => {
	let divs = document.querySelectorAll('.katalog__nomber');
	for (let d of divs){
		d.classList.toggle('active');
	} 
});