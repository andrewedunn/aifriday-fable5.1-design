/* ABOUTME: Builds the floorplan marker from the real room heights and tracks which room you're in.
   ABOUTME: Also gives the doorway photographs a small parallax so the thresholds have depth. */

(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rooms = Array.prototype.slice.call(document.querySelectorAll('.room'));
  var list = document.querySelector('.plan__list');

  /* ── floorplan: one bar per room, sized to how deep that room actually is ── */
  function drawPlan() {
    if (!list) return;
    var heights = rooms.map(function (r) { return r.offsetHeight; });
    var total = heights.reduce(function (a, b) { return a + b; }, 0);
    list.innerHTML = '';
    rooms.forEach(function (room, i) {
      var name = room.dataset.room || 'Room ' + (i + 1);
      var li = document.createElement('li');
      var btn = document.createElement('button');
      btn.className = 'plan__room';
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Go to: ' + name);
      var bar = document.createElement('span');
      bar.className = 'plan__bar';
      bar.style.height = Math.max(14, Math.round(heights[i] / total * 210)) + 'px';
      var label = document.createElement('span');
      label.className = 'plan__label';
      label.textContent = name;
      btn.appendChild(bar);
      btn.appendChild(label);
      btn.addEventListener('click', function () {
        room.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
      });
      li.appendChild(btn);
      list.appendChild(li);
    });
    markCurrent();
  }

  function markCurrent() {
    if (!list) return;
    var buttons = list.querySelectorAll('.plan__room');
    var mid = window.scrollY + window.innerHeight * 0.45;
    var active = 0;
    rooms.forEach(function (room, i) {
      if (room.offsetTop <= mid) active = i;
    });
    buttons.forEach(function (b, i) {
      b.setAttribute('aria-current', i === active ? 'true' : 'false');
    });
  }

  /* ── thresholds: the doorway photograph drifts against the wall behind it ── */
  var layers = Array.prototype.slice.call(
    document.querySelectorAll('.threshold img, .backdoor img')
  );

  function parallax() {
    var vh = window.innerHeight;
    layers.forEach(function (img) {
      var box = img.parentElement.getBoundingClientRect();
      if (box.bottom < -200 || box.top > vh + 200) return;
      // -1 when the band is entering from below, +1 when it is leaving above
      var progress = (vh - box.top) / (vh + box.height) * 2 - 1;
      progress = Math.max(-1, Math.min(1, progress));
      img.style.transform = 'translate3d(0,' + (progress * -22).toFixed(2) + 'px,0)';
    });
  }

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      markCurrent();
      if (!reduced) parallax();
      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { drawPlan(); onScroll(); });
  window.addEventListener('load', function () { drawPlan(); onScroll(); });
  drawPlan();
  onScroll();
})();
