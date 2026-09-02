// Counts the days to the next meetup so the date on the sign reads as a real
// upcoming Friday rather than a fact printed on a page. Nothing else.
(function () {
  var MEETUP = new Date(2026, 9, 2, 17, 30); // Friday, October 2, 2026, 5:30pm
  var el = document.getElementById('countdown');
  if (!el) return;

  var now = new Date();
  var startOfDay = function (d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate()); };
  var days = Math.round((startOfDay(MEETUP) - startOfDay(now)) / 86400000);

  if (days > 1) {
    el.textContent = days + ' days from today.';
  } else if (days === 1) {
    el.textContent = 'Tomorrow.';
  } else if (days === 0) {
    el.textContent = 'That is tonight.';
  } else {
    return; // Date has passed; say nothing rather than something wrong.
  }
  el.hidden = false;
})();
