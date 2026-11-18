/* Deepak Watch Center: small, dependency-free script.
   No cookies, no tracking, no data sent anywhere. */
(function () {
  "use strict";

  // Mobile menu
  var toggle = document.getElementById("menu-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
      }
    });
  }

  // Footer year
  var yr = document.getElementById("year");
  if (yr) yr.textContent = String(new Date().getFullYear());

  // Clock shows the current time in Nepal (UTC+05:45)
  var h = document.getElementById("hand-h"),
      m = document.getElementById("hand-m"),
      s = document.getElementById("hand-s");
  if (h && m && s) {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var tick = function () {
      var now = new Date(Date.now() + (5 * 60 + 45) * 60000);
      var sec = now.getUTCSeconds(), min = now.getUTCMinutes() + sec / 60, hr = (now.getUTCHours() % 12) + min / 60;
      h.setAttribute("transform", "rotate(" + (hr * 30) + " 200 200)");
      m.setAttribute("transform", "rotate(" + (min * 6) + " 200 200)");
      s.setAttribute("transform", "rotate(" + (sec * 6) + " 200 200)");
    };
    tick();
    if (!reduce) setInterval(tick, 1000);
    else setInterval(tick, 60000);
  }

  // Google Map loads only after the visitor asks for it
  var btn = document.getElementById("load-map");
  var box = document.getElementById("map");
  if (btn && box) {
    btn.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://maps.google.com/maps?q=28.7048389,80.5740302&z=17&output=embed";
      f.title = "Google Map showing Deepak Watch Center on Bus Park Road, Dhangadhi";
      f.loading = "lazy";
      f.referrerPolicy = "strict-origin-when-cross-origin";
      f.setAttribute("allowfullscreen", "");
      box.innerHTML = "";
      box.appendChild(f);
      f.focus();
    });
  }
})();
