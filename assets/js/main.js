(function ($) {
	"use strict";
	////////////////////////////////////////////////////
	// 03. Search Js
	$(".search-open-btn").on("click", function () {
		$(".search__popup").addClass("search-opened");
	});

	
	$(".search-close-btn").on("click", function () {
		$(".search__popup").removeClass("search-opened");
	});
	
	$(".job-form-open-btn").on("click", function () {
		$(".job__form").slideToggle("job__form");
	});

	$('.it-service-2-item').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.it-service-2-item').removeClass('active');
	});

	// $('.it-blog-2-item').on('mouseenter', function () {
	// 	$(this).addClass('active').parent().siblings().find('.it-blog-2-item').removeClass('active');
	// });


	var windowOn = $(window)
	///////////////////////////////////////////////////
	// 01. PreLoader Js
	windowOn.on('load',function () {
		$('#loading').fadeOut(500);
	});

	// 08. Nice Select Js
	$('select').niceSelect();

    ///////////////////////////////////////////////////
	// 03. scroll-to-target 
	windowOn.on('scroll', function () {
		var scroll = windowOn.scrollTop();
		if (scroll < 500) {
			$('.scroll-to-target').removeClass('open');

		} else {
			$('.scroll-to-target').addClass('open');
		}
	});

	if ($('.it-header-height').length > 0) {
		var headerHeight = document.querySelector(".it-header-height");
		var setHeaderHeight = headerHeight.offsetHeight;
		$(".it-header-height").each(function () {
			$(this).css({
				'height': setHeaderHeight + 'px'
			});
		});

		$(".it-header-height .header-sticky").each(function () {
			$(this).css({
				'height': inherit,
			});
		});
	}
	
	///////////////////////////////////////////////////
	// 04. Scroll Up Js
	if ($('.scroll-to-target').length) {
		$(".scroll-to-target").on('click', function () {
		var target = $(this).attr('data-target');
		// animate
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 1000);
	
		});
	}

	// 04. Scroll Up Js
	if ($('.scroll-to-target-2').length) {
		$(".scroll-to-target-2").on('click', function () {
		var target = $(this).attr('data-target');
		// animate
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 1000);
	
		});
	}
	function smoothSctollTop() {
		$('.smooth a').on('click', function (event) {
			var target = $(this.getAttribute('href'));
			if (target.length) {
				event.preventDefault();
				$('html, body').stop().animate({
					scrollTop: target.offset().top - 150
				}, 1000);
			}
		});
	}
	smoothSctollTop();
	
    ///////////////////////////////////////////////////
	// 05. wow animation
	var wow = new WOW(
		{
		  mobile: true,
		}
	  );
	  wow.init();
	var windowOn = $(window);

	///////////////////////////////////////////////////
	// 06. PreLoader Js
	windowOn.on('load',function() {
		$("#loading").fadeOut(500);

	});

	///////////////////////////////////////////////////
	// 07. Sticky Header Js
	windowOn.on('scroll', function () {
		var scroll = windowOn.scrollTop();
		if (scroll < 400) {
			$("#header-sticky").removeClass("header-sticky");
		} else {
			$("#header-sticky").addClass("header-sticky");
		}
	});

	
	$(window).on('load', function () {

		$('#preloader').delay(350).fadeOut('slow');

		$('body').delay(350).css({ 'overflow': 'visible' });

	})

	////////////////////////////////////////////////////
	// 09. Sidebar Js
	$(".it-menu-bar").on("click", function () {
		$(".itoffcanvas").addClass("opened");
		$(".body-overlay").addClass("apply");
	});
	$(".close-btn").on("click", function () {
		$(".itoffcanvas").removeClass("opened");
		$(".body-overlay").removeClass("apply");
	});
	$(".body-overlay").on("click", function () {
		$(".itoffcanvas").removeClass("opened");
		$(".body-overlay").removeClass("apply");
	});


	if($('.it-menu-content').length && $('.it-menu-mobile').length){
		let navContent = document.querySelector(".it-menu-content").outerHTML;
		let mobileNavContainer = document.querySelector(".it-menu-mobile");
		mobileNavContainer.innerHTML = navContent;
	
		let arrow = $(".it-menu-mobile .has-dropdown > a");
	
		arrow.each(function () {
			let self = $(this);
			let arrowBtn = document.createElement("BUTTON");
			arrowBtn.classList.add("dropdown-toggle-btn");
			arrowBtn.innerHTML = "<i class='fal fa-angle-right'></i>";
			self.append(function () {
			  return arrowBtn;
			});
	
			self.find("button").on("click", function (e) {
			  e.preventDefault();
			  let self = $(this);
			  self.toggleClass("dropdown-opened");
			  self.parent().toggleClass("expanded");
			  self.parent().parent().addClass("dropdown-opened").siblings().removeClass("dropdown-opened");
			  self.parent().parent().children(".it-submenu").slideToggle();
			});
	
		});
	}

	///////////////////////////////////////////////////
	// 10. Magnific Js
	$(".popup-video").magnificPopup({
		type: "iframe",
	});
	
	////////////////////////////////////////////////////
	// 14. magnificPopup Js
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});


	////////////////////////////////////////////////////
	// 11. Data CSS Js
	$("[data-background").each(function () {
		$(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
	});

	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"));
	});

	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"));
	});

	////////////////////////////////////////////////////
	// 12. Counter Js
	if ($(".purecounter").length) {
		new PureCounter({
			filesizing: true,
			selector: ".filesizecount",
			pulse: 2,
		});
		new PureCounter();
	}

	function mediaSize() { 
		/* Set the matchMedia */
		if (window.matchMedia('(min-width: 768px)').matches) {
			const panels = document.querySelectorAll('.col-custom')
			panels.forEach(panel => {
				panel.addEventListener('mouseenter', () => {
					removeActiveClasses()
					panel.classList.add('active')
				})
			})
		
			function removeActiveClasses() {
				panels.forEach(panel => {
					panel.classList.remove('active')
				})
			}

		} else {
		/* Reset for CSS changes â€“ Still need a better way to do this! */
			$(".col-custom ").addClass("active");
		}
	};
	/* Call the function */
	mediaSize();
	/* Attach the function to the resize event listener */
	  window.addEventListener('resize', mediaSize, false); 



	////////////////////////////////////////////////////
	// 13. Swiper Js
	const postboxswiper = new Swiper('.postbox__thumb-slider-active', {
		// Optional parameters
		speed:500,
		loop: true,
		slidesPerView: 1,
        spaceBetween:0,
		autoplay: true,
		roundLengths: true,
		effect:'fade',
		breakpoints: {
			'1400': {
				slidesPerView: 1,
			},
			'1200': {
				slidesPerView: 1,
			},
			'992': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		navigation: {
			prevEl: '.postbox-arrow-prev',
			nextEl: '.postbox-arrow-next',
		},
	  });
	////////////////////////////////////////////////////

	// 13. Swiper Js
	const brandswiper = new Swiper('.it-brand-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 4,
        spaceBetween: 30,
		autoplay: true,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 4,
			},
			'1200': {
				slidesPerView: 4,
			},
			'992': {
				slidesPerView: 3,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 2,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	  });
	////////////////////////////////////////////////////
	// 13. Swiper Js
	const blog2sswiper = new Swiper('.it-blog-2-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 3,
        spaceBetween: 30,
		autoplay: false,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 3,
			},
			'1200': {
				slidesPerView: 3,
				spaceBetween: 50,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
				spaceBetween: 50,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	  });
	////////////////////////////////////////////////////
	// 13. Swiper Js
	const team2sswiper = new Swiper('.it-team-2-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 3,
        spaceBetween: 30,
		autoplay: true,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 3,
			},
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		pagination: {
			el: ".it-team-dots",
			clickable:true,
		  },
	  });
	////////////////////////////////////////////////////
	// 13. Swiper Js
	const testimonial2swiper = new Swiper('.it-testimonial-2-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 1,
        spaceBetween: 60,
		autoplay: true,
		centeredSlides: true,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 1,
			},
			'1200': {
				slidesPerView: 1,
			},
			'992': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		pagination: {
			el: ".it-testimonial-2-dots",
			clickable:true,
		  },
	  });

	////////////////////////////////////////////////////
	// 13. Swiper Js
	const sliderswiper = new Swiper('.it-slider-active', {
		// Optional parameters
		speed:1000,
		loop: true,
		slidesPerView: 1,
		autoplay: true,
		roundLengths: true,
		effect:'fade',
		breakpoints: {
			'1400': {
				slidesPerView: 1,
			},
			'1200': {
				slidesPerView: 1,
			},
			'992': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		navigation: {
			prevEl: '.classes-prev',
			nextEl: '.classes-next',
		},
		pagination: {
			el: ".it-classes-dots",
			clickable:true,
		  },
	  });
	////////////////////////////////////////////////////
	// 13. Swiper Js
	const classesswiper = new Swiper('.it-classes-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 3,
        spaceBetween: 30,
		autoplay: true,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 3,
			},
			'1200': {
				slidesPerView: 2,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		navigation: {
			prevEl: '.classes-prev',
			nextEl: '.classes-next',
		},
		pagination: {
			el: ".it-classes-dots",
			clickable:true,
		  },
	  });

	////////////////////////////////////////////////////
	// 13. Swiper Js
	const testiswiper = new Swiper('.it-testimonial-active', {
		// Optional parameters
		speed:1500,
		loop: true,
		slidesPerView: 1,
        spaceBetween: 30,
		autoplay: true,
		centeredSlides: true,
		roundLengths: true,
		breakpoints: {
			'1400': {
				slidesPerView: 1,
			},
			'1200': {
				slidesPerView: 1,
			},
			'992': {
				slidesPerView: 1,
			},
			'768': {
				slidesPerView: 1,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
		navigation: {
			prevEl: '.testimonial-prev',
			nextEl: '.testimonial-next',
		},
	  });


	$('.it-funtact-item').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.it-funtact-item').removeClass('active');
	});

	$('.it-service-2-item').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.it-service-2-item').removeClass('active');
	});
	$('.it-funfact-3-item-box').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.it-funfact-3-item-box').removeClass('active');
	});

	////////////////////////////////////////////////////
	// 14. magnificPopup Js
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});


	// 20. Show Login Toggle Js
	$('#showlogin').on('click', function () {
		$('#checkout-login').slideToggle(900);
	});

	/*-------------------------

		showcoupon toggle function

	--------------------------*/

	$('#showcoupon').on('click', function () {

		$('#checkout_coupon').slideToggle(900);
	});


/*-------------------------

	Create an account toggle function

--------------------------*/

$('#cbox').on('click', function () {

	$('#cbox_info').slideToggle(900);

});



/*-------------------------

	Create an account toggle function

--------------------------*/

$('#ship-box').on('click', function () {

	$('#ship-box-info').slideToggle(1000);

});


	////////////////////////////////////////////////////
	// 15. MagnificPopup video view Js
	$(".popup-video").magnificPopup({
	   type: "iframe",
    });

	////////////////////////////////////////////////////
	//26.isotope
	$('.grid').imagesLoaded(function () {
		// init Isotope
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			percentPosition: true,
			masonry: {
				columnWidth: '.grid-item',
			},
			
		});
		// filter items on button click
		$('.masonary-menu').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ 
				filter: filterValue,
				animationOptions: {
					duration: 100,
					easing: "linear",
					queue: true
				}
			});
			
		});
		//for menu active class
		$('.masonary-menu button').on('click', function (event) {
			$(this).siblings('.active').removeClass('active');
			$(this).addClass('active');
			event.preventDefault();
		});

	});	
		
	// 05. Search Js
	$(".accordion-items").on("click", function () {
		$(".accordion-items").toggleClass("open");
	});
	$(".accordion-items").on("click", function () {
		$(".accordion-items").removeClass("open");
	});

	////////////////////////////////////////////////////
	// 16. Cart Quantity Js
	$('.it-cart-minus').on('click', function () {
		var $input = $(this).parent().find('input');
		var count = parseInt($input.val()) - 1;
		count = count < 1 ? 1 : count;
		$input.val(count);
		$input.change();
		return false;
	});

	$('.it-cart-plus').on('click', function () {
		var $input = $(this).parent().find('input');
		$input.val(parseInt($input.val()) + 1);
		$input.change();
		return false;
	});

	


		if($('.it-main-menu-content').length && $('.it-main-menu-mobile').length){
		let navContent = document.querySelector(".it-main-menu-content").outerHTML;
		let mobileNavContainer = document.querySelector(".it-main-menu-mobile");
		mobileNavContainer.innerHTML = navContent;


		let arrow = $(".it-main-menu-mobile .has-dropdown > a");

		arrow.each(function () {
			let self = $(this);
			let arrowBtn = document.createElement("BUTTON");
			arrowBtn.classList.add("dropdown-toggle-btn");
			arrowBtn.innerHTML = "<i class='fal fa-angle-right'></i>";

			self.append(function () {
				return arrowBtn;
			});

			self.find("button").on("click", function (e) {
				e.preventDefault();
				let self = $(this);
				self.toggleClass("dropdown-opened");
				self.parent().toggleClass("expanded");
				self.parent().parent().addClass("dropdown-opened").siblings().removeClass("dropdown-opened");
				self.parent().parent().children(".it-submenu").slideToggle();
			});

		});
	}
	// for header
	if ($("#it-header-top-lang").length > 0) {
		window.addEventListener('click', function (e) {

			if (document.getElementById('it-header-top-lang').contains(e.target)) {
				$(".it-header-top-lang").toggleClass("open");
			}
			else {
				$(".it-header-top-lang").removeClass("open");
			}
		});
	}	

	$('.it-class-item').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.it-class-item').removeClass('active');
	});


	//One Page Scroll Js
	function scrollNav() {
		$('.onepage-menu li').click(function () {
			$(".onepage-menu li.active").removeClass("active");
			$(this).addClass("active");

			$('html, body').stop().animate({
				scrollTop: $($(this).attr('href')).offset().top - 80
			}, 300);
			return false;
		});
	}
	scrollNav();


	if ($('[data-mask-src]').length > 0) {
		$('[data-mask-src]').each(function () {
		  var mask = $(this).attr('data-mask-src');
		  $(this).css({
			'mask-image': 'url(' + mask + ')',
			'-webkit-mask-image': 'url(' + mask + ')'
		  });
		  $(this).removeAttr('data-mask-src');
		});
	};
	

	////////////////////////////////////////////////////
// 20. Brand Slider Activation
var brand = new Swiper('.it-brand-slider', {
    slidesPerView: 5,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 3000,
    },
    breakpoints: {
        '1200': {
            slidesPerView: 5,
        },
        '992': {
            slidesPerView: 4,
        },
        '768': {
            slidesPerView: 3,
        },
        '576': {
            slidesPerView: 2,
        },
        '0': {
            slidesPerView: 1,
        },
    },
});



/* ===== YouTube Carousel (thumb path only, 10 videos, loop + autoplay) ===== */
(function(){
  // ---- Config ----
  const REQUIRED_W=1280, REQUIRED_H=720;
  const PLACEHOLDER="assets/img/yt/thumbs/_placeholder_1280x720.png";
  const CFG = {
    loop:true,
    autoplay:true,
    interval:4500,
    pauseOnHover:true,
    pauseOnInteract:true
  };

  // ---- Data: 10 video (ganti sesuai punyamu) ----
  const videos = [
    { url:"https://www.youtube.com/watch?v=dQw4w9WgXcQ", thumbPath:"assets/img/yt/thumbs/01_rick_1280x720.png" },
    { url:"https://youtu.be/9bZkp7q19f0",               thumbPath:"assets/img/yt/thumbs/02_gangnam_1280x720.jpg" },
    { url:"https://www.youtube.com/watch?v=3JZ_D3ELwOQ",thumbPath:"assets/img/yt/thumbs/03_see_you_again_1280x720.jpg" },
    { url:"https://youtu.be/fJ9rUzIMcZQ",               thumbPath:"assets/img/yt/thumbs/04_bohemian_1280x720.png" },
    { url:"https://www.youtube.com/watch?v=kXYiU_JCYtU",thumbPath:"assets/img/yt/thumbs/05_numb_1280x720.jpg" },
    { url:"https://www.youtube.com/watch?v=JGwWNGJdvx8",thumbPath:"assets/img/yt/thumbs/06_shape_of_you_1280x720.jpg" },
    { url:"https://youtu.be/CevxZvSJLk8",               thumbPath:"assets/img/yt/thumbs/07_roar_1280x720.png" },
    { url:"https://www.youtube.com/watch?v=OPf0YbXqDm0",thumbPath:"assets/img/yt/thumbs/08_uptown_funk_1280x720.jpg" },
    { url:"https://youtu.be/2Vv-BfVoq4g",               thumbPath:"assets/img/yt/thumbs/09_perfect_1280x720.jpg" },
    { url:"https://www.youtube.com/watch?v=hTWKbfoikeg",thumbPath:"assets/img/yt/thumbs/10_spirit_1280x720.png" }
  ];

  // ---- Helpers ----
  const $  = s => document.querySelector(s);
  const $$ = s => document.querySelectorAll(s);
  function ytId(u){
    try{
      const x = new URL(u);
      if(x.hostname.includes("youtu.be")) return x.pathname.slice(1);
      if(x.searchParams.get("v")) return x.searchParams.get("v");
      const p=x.pathname.split("/"); const i=p.findIndex(t=>["embed","shorts","live"].includes(t));
      if(i>=0 && p[i+1]) return p[i+1];
    }catch(e){}
    return "";
  }
  const ytEmbed = (id,auto=1)=>`https://www.youtube.com/embed/${id}?`+[
    'autoplay='+(auto?1:0),
    'controls=0',
    'rel=0',
    'modestbranding=1',
    'fs=1',
    'playsinline=1',
    'disablekb=1',
    'showinfo=0',
    'iv_load_policy=3',
    `origin=${encodeURIComponent(location.origin)}`
  ].join('&');

  function thumbOf(v){ return (v.thumbPath && v.thumbPath.trim()) ? v.thumbPath : PLACEHOLDER; }

  // ---- DOM refs ----
  const track=$("#ytTrack"), dots=$("#ytDots"), viewport=$("#ytViewport");
  const btnPrev=$("#ytPrev"), btnNext=$("#ytNext");
  const modal=$("#ytModal"), player=$("#ytPlayer"), closeBtn=$("#ytClose");

  // ---- State ----
  const state={index:0,pages:0,per:1,slideW:0,drag:false,sx:0,stx:0};
  const perPage=()=>{ const w=viewport.clientWidth; const cw=Math.max(260, Math.min(360, w*0.6)); return Math.max(1, Math.floor(w/(cw+16))); };

  // ---- Render ----
  function render(){
    track.innerHTML="";
    videos.forEach(v=>{
      const id=ytId(v.url);
      const card=document.createElement("article");
      card.className="it-ytc__card"; card.dataset.vid=id;
      card.innerHTML=`
        <div class="it-ytc__warn" hidden>Ukuran bukan 1280×720</div>
        <a class="it-ytc__thumb" href="${v.url}" target="_blank" rel="noopener" aria-label="Buka di YouTube">
          <img loading="eager" src="${thumbOf(v)}" alt="">
          <span class="it-ytc__play">
            <button class="it-ytc__btn" type="button" data-play="${id}" aria-label="Putar">
              <svg viewBox="0 0 100 100" aria-hidden="true">
                <polygon points="40,30 40,70 75,50" fill="white" fill-opacity="0.9"/>
              </svg>
            </button>
          </span>
        </a>`;
      // validasi dimensi thumbnail
      const img=card.querySelector("img"), warn=card.querySelector(".it-ytc__warn");
      img.addEventListener("load", ()=>{ warn.hidden = (img.naturalWidth===REQUIRED_W && img.naturalHeight===REQUIRED_H); });
      track.appendChild(card);
    });

    // dots & layout
    dots.innerHTML="";
    updateLayout();
    for(let p=0;p<state.pages;p++){
      const b=document.createElement("button"); b.className="it-ytc__dot"; b.setAttribute("role","tab");
      b.setAttribute("aria-label",`Halaman ${p+1}`); if(p===state.index) b.setAttribute("aria-current","true");
      b.addEventListener("click", ()=>go(p)); dots.appendChild(b);
    }
    updateArrows();
    startAutoplay();
  }

  function updateLayout(){
    if(!track.children.length) return;
    state.per = perPage();
    const cW = track.children[0].getBoundingClientRect().width;
    state.slideW = cW + 16;
    state.pages = Math.max(1, Math.ceil(videos.length/state.per));
    if (!CFG.loop) clamp();
    apply(); refreshDots();
  }
  function clamp(){ if(state.index<0) state.index=0; if(state.index>state.pages-1) state.index=state.pages-1; }
  function apply(tx){ const off=-(state.index*(state.slideW*state.per)); track.style.transform=`translate3d(${(tx??off)}px,0,0)`; }
  function refreshDots(){ [...dots.children].forEach((d,i)=> i===state.index?d.setAttribute("aria-current","true"):d.removeAttribute("aria-current")); }
  function updateArrows(){
    if (CFG.loop) { btnPrev.disabled=false; btnNext.disabled=false; }
    else { btnPrev.disabled=(state.index===0); btnNext.disabled=(state.index===state.pages-1); }
  }
  function go(i){
    if (CFG.loop){
      const P = state.pages || 1;
      state.index = ((i % P)+P)%P;
    } else {
      state.index = i; clamp();
    }
    apply(); refreshDots(); updateArrows();
  }

  // tombol
  btnPrev.addEventListener("click", ()=>go(state.index-1));
  btnNext.addEventListener("click", ()=>go(state.index+1));

  // drag / swipe
  function down(x){ state.drag=true; state.sx=x; const m=/translate3d\(([-0-9.]+)px/.exec(getComputedStyle(track).transform); state.stx=m?parseFloat(m[1]):0; document.body.classList.add("dragging"); if(CFG.pauseOnInteract) isInteracting=true; }
  function move(x){ if(!state.drag) return; const dx=x-state.sx; apply(state.stx+dx); }
  function up(x){ if(!state.drag) return; const dx=x-state.sx; state.drag=false; document.body.classList.remove("dragging"); const th=state.slideW*0.25; if(dx<-th) go(state.index+1); else if(dx>th) go(state.index-1); else apply(); if(CFG.pauseOnInteract) isInteracting=false; }
  viewport.addEventListener("mousedown", e=>down(e.clientX));
  window.addEventListener("mousemove", e=>move(e.clientX));
  window.addEventListener("mouseup",   e=>up(e.clientX));
  viewport.addEventListener("touchstart", e=>down(e.touches[0].clientX), {passive:true});
  window.addEventListener("touchmove",  e=>move(e.touches[0].clientX), {passive:true});
  window.addEventListener("touchend",   e=>up(state.sx), {passive:true});

  // modal player
  track.addEventListener("click", e=>{
    const btn=e.target.closest("button[data-play]"); if(!btn) return;
    e.preventDefault(); const id=btn.getAttribute("data-play");
    player.innerHTML=`<iframe width="100%" height="100%" src="${ytEmbed(id,1)}" title="YouTube player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>`;
    modal.classList.add("open"); closeBtn.focus();
  });
  function close(){ modal.classList.remove("open"); player.innerHTML=""; }
  modal.addEventListener("click", e=>{ if(e.target===modal) close(); });
  closeBtn.addEventListener("click", close);
  window.addEventListener("keydown", e=>{ if(e.key==="Escape" && modal.classList.contains("open")) close(); if(e.key==="ArrowLeft") go(state.index-1); if(e.key==="ArrowRight") go(state.index+1); });

  // autoplay
  let autoTimer=null, isHover=false, isInteracting=false;
  function startAutoplay(){
    if (!CFG.autoplay) return;
    stopAutoplay();
    autoTimer=setInterval(()=>{
      if(isHover||isInteracting||state.pages<=1) return;
      go(state.index+1);
    }, CFG.interval);
  }
  function stopAutoplay(){ if(autoTimer){ clearInterval(autoTimer); autoTimer=null; } }

  if (CFG.pauseOnHover){
    viewport.addEventListener("mouseenter", ()=>{ isHover=true; });
    viewport.addEventListener("mouseleave", ()=>{ isHover=false; });
  }
  if (CFG.pauseOnInteract){
    viewport.addEventListener("mousedown", ()=>{ isInteracting=true; });
    window.addEventListener("mouseup", ()=>{ isInteracting=false; });
    viewport.addEventListener("touchstart", ()=>{ isInteracting=true; }, {passive:true});
    window.addEventListener("touchend", ()=>{ isInteracting=false; }, {passive:true});
  }
  // pause kalau modal buka
  new MutationObserver(()=>{ modal.classList.contains("open") ? stopAutoplay() : startAutoplay(); })
    .observe(modal, {attributes:true, attributeFilter:["class"]});

  // init
  render();
  let rid; window.addEventListener("resize", ()=>{ cancelAnimationFrame(rid); rid=requestAnimationFrame(()=>{ updateLayout(); startAutoplay(); }); });
})();


})(jQuery);