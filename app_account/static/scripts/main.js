/* MODAL for Log In */
const modal = document.querySelector('.modal');
const closeButtons = document.querySelectorAll('.close-modal');

document.querySelector('.open-modal').addEventListener('click', function(){
  modal.classList.toggle('modal-open');
});

for (i=0; i<closeButtons.length; ++i){
  closeButtons[i].addEventListener('click', function(){
    modal.classList.toggle(modal-open);
  });
}

document.querySelector('.modal-inner').addEventListener('click', function(){
  modal.classList.toggle('modal-open');
});

document.querySelector('.modal-content').addEventListener('click', function(e){
  e.stopPropagation();
})