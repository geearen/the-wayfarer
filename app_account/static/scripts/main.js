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

//Dropdown

function myFunction() {
  document.getElementById("dropdown_content").classList.toggle("show");
}

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


// Truncate Posts

function readMore(pk) {
  let selectedId = `#${pk}`
  if ($(".post_tips_button").is(selectedId) && ){}
  // $(".post_tips_button ").click(function(event){
  //   event.stopPropagation();
  //   console.log(event.isPropagationStopped());
    if(!$(".post_tips_button").is("#read_less")){
      $(".post_tips p").removeClass("post_tips_truncate");
      $(".post_tips_button").text("read less");
      $(".post_tips_button").attr("id", "read_less");
    }else {
      $(".post_tips_button").text("read more");
      $(".post_tips p").addClass("post_tips_truncate");
      $(".post_tips_button").removeAttr("read_less");
    };
  });
}

$(".post_tips_button").click(function(e){
  if(!$(".post_tips_button").is("#read_less")){
  $(".city_post_container p").removeClass("post_tips_truncate");
  $(".post_tips_button").text("read less");
  $(".post_tips_button").attr("id", "read_less");

  }else {
    $(".post_tips_button").text("read more");
    $(".city_post_container p").addClass("post_tips_truncate");
    $(".post_tips_button").removeAttr("read_less");
  };
  e.stopPropagation();
});
