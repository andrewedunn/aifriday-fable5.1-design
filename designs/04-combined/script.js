// ABOUTME: Scroll behaviour for the AI Friday homepage.
// ABOUTME: Rooms settle as you enter them; doorways gain a little depth as you pass through.

(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches) return;

  document.documentElement.classList.add('js');

  // Rooms settle when you walk into them.
  var rooms = document.querySelectorAll('.room__inner');

  if ('IntersectionObserver' in window) {
    var watcher = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        watcher.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.06 });

    rooms.forEach(function (room) { watcher.observe(room); });
  } else {
    rooms.forEach(function (room) { room.classList.add('is-in'); });
  }

  // Doorways open very slightly as they cross the middle of the screen, so
  // passing one has depth. Small enough to feel and not to notice.
  var doors = Array.prototype.slice.call(document.querySelectorAll('.door'));
  if (!doors.length) return;

  var ticking = false;

  function drawDoors() {
    ticking = false;
    var h = window.innerHeight;

    doors.forEach(function (door) {
      var box = door.getBoundingClientRect();
      if (box.bottom < -80 || box.top > h + 80) return;

      // 0 when the door is entering from below, 1 when it has passed above.
      var travelled = (h - box.top) / (h + box.height);
      var clamped = travelled < 0 ? 0 : travelled > 1 ? 1 : travelled;
      door.style.setProperty('--door-scale', (1 + clamped * 0.07).toFixed(4));
    });
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(drawDoors);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  drawDoors();
})();
