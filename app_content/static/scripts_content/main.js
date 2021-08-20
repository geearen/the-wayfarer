
// Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

const caroselImages = [
  {
    src:"https://images.unsplash.com/photo-1523590564318-491748f70ea7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
    alt: ""
  },
  {
    src:"https://images.unsplash.com/photo-1527251672045-a80241b3f574?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
    alt: ""
  },
  {
    src:"https://images.unsplash.com/photo-1431102996501-f6379b157668?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80",
    alt: ""
  },
  {
    src:"https://images.unsplash.com/photo-1602775112551-fa7515719bf6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80",
    alt: ""
  },
];

// function carousel(img) {
//   const image = caroselImages;
//   const index = 1

//   for (i = 0; i < image.length; i++) {
//     image[i].css("display" = "none");
//   }
// }



// const carouselIndex = 1;
// altCarousel(carouselIndex);

// // Next/previous controls
// function alternate(n) {
//   altCarousel(carouselIndex += n).on();
// }


// function altCarousel(n) {
//   let i = 1;
//   const $image = $(".carousel_images, img");
  
//   if (n > $image.length) {carouselIndex = 1}
//   if (n < 1) {carouselIndex = $image.length}
//   for (i = 0; i < $image.length; i++) {
//     $image[i].css("display" = "none");
//   }

//   $image[carouselIndex-1].css("display" = "block");
// }


let carouselIndex = 0;
altCarousel();

function altCarousel() {
  let i;
  let slides = document.getElementsByClassName("carousel_images");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  carouselIndex++;
  if (carouselIndex > slides.length) {carouselIndex = 1}
  slides[carouselIndex-1].style.display = "block";
  setTimeout(altCarousel, 2000)}; 