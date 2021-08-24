// const carouselImages = [
//   {
//     src:"https://images.unsplash.com/photo-1523590564318-491748f70ea7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
//     alt: ""
//   },
//   {
//     src:"https://images.unsplash.com/photo-1527251672045-a80241b3f574?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
//     alt: ""
//   },
//   {
//     src:"https://images.unsplash.com/photo-1431102996501-f6379b157668?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
//     alt: ""
//   },
//   {
//     src:"https://images.unsplash.com/photo-1602775112551-fa7515719bf6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
//     alt: ""
//   },
// ];

const carouselImages = [
  {
    src:"/static/assets/Carosel.png",
    alt: ""
  },
  {
    src:"/static/assets/Carosel_2.png",
    alt: ""
  },
  {
    src:"/static/assets/Carosel_3.png",
    alt: ""
  },
  {
    src:"/static/assets/Carosel_4.png",
    alt: ""
  },
];


let idx = 0;

$('#carousel_button_right').click(function(arr) {
  arr = carouselImages
  idx++;
  if (idx >= arr.length) {
    idx = 0;
  }
  const $image = $(".carousel_images img");
  $image.attr('src', arr[idx].src);
});

$('#carousel_button_left').click(function(arr) {
  arr = carouselImages
  idx--;
  if (idx <= 0) {
    idx = arr.length - 1;
  }
  const $image = $(".carousel_images img");
  $image.attr('src', arr[idx].src);
});

const altCarousel = function altCarousel() {
  arr = carouselImages;
  idx++;
  if (idx >= arr.length) {
    idx = 0;
  }
  const $image = $(".carousel_images img");
  $image.attr('src', arr[idx].src);

}

setInterval(altCarousel, 4000);

/* MODAL for Log In */
const modal = document.querySelector('.modal');
const closeButtons = document.querySelectorAll('.close-modal');


document.querySelector('.open-modal').addEventListener('click', function(){
  modal.classList.toggle('modal-open');
});

for (i=0; i<closeButtons.length; ++i){
  closeButtons[i].addEventListener('click', function(){
    modal.classList.toggle('modal-open');
  });
}

document.querySelector('.modal-inner').addEventListener('click', function(){
  modal.classList.toggle('modal-open');
});

$(".modal-content").click(function (event){
  event.stopPropagation();
})


// Dropdown Menu 


// $("#dropdown_i").click(function(){
//   $(".dropdown_content a").toggle("show")
// });


function myFunction() {
  document.getElementById("dropdown_content").classList.toggle("show");
  console.log('this works');
}


window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    let i;
    for (i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
  event.stopPropagation();
}


