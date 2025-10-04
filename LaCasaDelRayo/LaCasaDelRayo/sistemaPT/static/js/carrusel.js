let slideIndex = 0;
let slides = document.getElementsByClassName("mySlides");
let dots = document.getElementsByClassName("dot");

function initCarousel() {
    if (slides.length === 0) return; // Evita errores
    // Mostrar primer slide
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex = 0;
    slides[slideIndex].style.display = "block";
    if (dots.length) dots[slideIndex].className += " active";

    showSlidesAuto(); // Inicia autoplay
}

function showSlidesAuto() {
    for (let i = 0; i < slides.length; i++) slides[i].style.display = "none";
    slideIndex++;
    if (slideIndex >= slides.length) slideIndex = 0;
    slides[slideIndex].style.display = "block";
    if (dots.length) {
        for (let i = 0; i < dots.length; i++) dots[i].className = dots[i].className.replace(" active", "");
        dots[slideIndex].className += " active";
    }
    setTimeout(showSlidesAuto, 3000);
}

function plusSlides(n) {
    slideIndex += n - 1;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    showSlidesManual();
}

function currentSlide(n) {
    slideIndex = n - 1;
    showSlidesManual();
}

function showSlidesManual() {
    for (let i = 0; i < slides.length; i++) slides[i].style.display = "none";
    slides[slideIndex].style.display = "block";
    if (dots.length) {
        for (let i = 0; i < dots.length; i++) dots[i].className = dots[i].className.replace(" active", "");
        dots[slideIndex].className += " active";
    }
}

// Inicializar carrusel cuando la página cargue
window.onload = initCarousel;
