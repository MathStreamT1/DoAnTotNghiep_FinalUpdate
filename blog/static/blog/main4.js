 // Add a class to each timeline item to trigger the animation
 document.addEventListener("DOMContentLoaded", function() {
  const timelineItems = document.querySelectorAll('.timeline-item');
  timelineItems.forEach((item, index) => {
    setTimeout(() => {
      item.classList.add('show');
    }, index * 1000); // Adjust the delay between each item
  });
});
// Add a class to trigger the fade-in animation after reading previous content
document.addEventListener("DOMContentLoaded", function() {
  const content = document.querySelector('.fade-in');
  const isInViewport = function(element) {
    const bounding = element.getBoundingClientRect();
    return (
      bounding.top >= 0 &&
      bounding.left >= 0 &&
      bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  };

  const addFadeInClass = function() {
    if (isInViewport(content)) {
      content.classList.add('show');
      window.removeEventListener('scroll', addFadeInClass);
    }
  };

  window.addEventListener('scroll', addFadeInClass);
});

  // Add a class when the element is in view
  function checkInView() {
    $(".roadmap-item").each(function() {
      var windowHeight = $(window).height();
      var scrollPosition = $(window).scrollTop();
      var offset = $(this).offset().top;

      if (scrollPosition > offset - windowHeight + 100) {
        $(this).addClass("in-view");
      }
    });

  // Trigger the function on scroll
  $(window).scroll(function() {
    checkInView();
  });

  // Trigger the function on page load
  checkInView();
};