// ASBB shared site scripts
(function () {
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.classList.toggle('active', open);
      burger.setAttribute('aria-expanded', open);
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        burger.classList.remove('active');
        burger.setAttribute('aria-expanded', false);
      });
    });
  }
  // Newsletter (front-end only — connect to email platform on launch)
  var form = document.getElementById('news-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = document.getElementById('news-msg');
      if (msg) msg.textContent = "Thanks for signing up — we'll be in touch. (Connect this form to your email platform on launch.)";
      form.reset();
    });
  }
})();
