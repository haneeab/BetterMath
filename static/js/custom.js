
  (function ($) {
  
  "use strict";

    // NAVBAR
    $('.navbar-nav .nav-link').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();

        if (scroll >= 50) {
            $(".navbar").addClass("sticky-nav");
        } else {
            $(".navbar").removeClass("sticky-nav");
        }
    });

    // BACKSTRETCH SLIDESHOW
    $('#section_1').backstretch([
          "{% static 'images/a.jpeg' %}",
          "{% static 'images/b.jpeg' %}",
          "{% static 'images/c.jpeg' %}"
        ],  {duration: 2000, fade: 750});
    
  })(window.jQuery);


