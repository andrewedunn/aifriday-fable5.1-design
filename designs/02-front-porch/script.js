// ABOUTME: Small progressive enhancements for the AI Friday page.
// ABOUTME: Section reveals on scroll, and the invitation settling in on load. Motion is optional.

(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var targets = document.querySelectorAll(
    '.hero__line, .hero__sub, .invite, .step .wrap, .table__head, .photo--table, .made__item, .leave__item, .ceiling__body, .sidewalk__col'
  );

  if (reduced || !('IntersectionObserver' in window)) return;

  targets.forEach(function (el, i) {
    el.classList.add('reveal');
    el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + 'ms';
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

  targets.forEach(function (el) { io.observe(el); });
})();
