(function () {
  var carousel = document.getElementById("home-carousel");
  if (!carousel) return;

  var slides = carousel.querySelectorAll(".carousel-slide");
  var dots = carousel.querySelectorAll(".dot");
  var current = 0;
  var timer = null;

  function show(index) {
    current = (index + slides.length) % slides.length;
    slides.forEach(function (slide, i) {
      slide.classList.toggle("active", i === current);
    });
    dots.forEach(function (dot, i) {
      dot.classList.toggle("active", i === current);
    });
  }

  function next() {
    show(current + 1);
  }

  function restart() {
    if (timer) clearInterval(timer);
    timer = setInterval(next, 5000);
  }

  var prev = carousel.querySelector(".carousel-prev");
  var nextBtn = carousel.querySelector(".carousel-next");
  if (prev) prev.addEventListener("click", function () { show(current - 1); restart(); });
  if (nextBtn) nextBtn.addEventListener("click", function () { show(current + 1); restart(); });

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () { show(i); restart(); });
  });

  restart();
})();
