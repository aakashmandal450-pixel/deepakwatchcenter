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

/* Brand tabs and photo viewer */
(function () {
  "use strict";
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".brand-tab"));
  function select(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
      var p = document.getElementById(t.getAttribute("aria-controls"));
      if (p) p.hidden = !on;
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () { select(t, false); });
    t.addEventListener("keydown", function (e) {
      var n = null;
      if (e.key === "ArrowRight") n = tabs[(i + 1) % tabs.length];
      else if (e.key === "ArrowLeft") n = tabs[(i - 1 + tabs.length) % tabs.length];
      else if (e.key === "Home") n = tabs[0];
      else if (e.key === "End") n = tabs[tabs.length - 1];
      if (n) { e.preventDefault(); select(n, true); }
    });
  });

  var box = document.getElementById("lightbox");
  if (!box || typeof box.showModal !== "function") return;
  var img = document.getElementById("lightbox-img");
  var cap = document.getElementById("lightbox-cap");
  var last = null;
  document.addEventListener("click", function (e) {
    var b = e.target.closest(".shot");
    if (!b) return;
    var thumb = b.querySelector("img");
    last = b;
    img.src = b.getAttribute("data-full");
    img.alt = thumb ? thumb.alt : "";
    cap.textContent = b.getAttribute("data-caption") || "";
    box.showModal();
  });
  document.getElementById("lightbox-close").addEventListener("click", function () { box.close(); });
  box.addEventListener("click", function (e) { if (e.target === box) box.close(); });
  box.addEventListener("close", function () { if (last) last.focus(); });
})();
