"""Builds the static pages from one shared header and footer.
Run: python3 build.py  (outputs index.html, privacy.html, terms.html, 404.html)"""

DOMAIN = "https://deepakwatchcenter.com.np"
PHONE_M = "984-8420742"; TEL_M = "+9779848420742"
PHONE_L = "091-525060";  TEL_L = "+97791525060"
ADDRESS = "Bus Park Road, Dhangadhi, Kailali, Sudurpashchim Province 10900, Nepal"
MAPS = "https://maps.app.goo.gl/YZKGEJjhBLyE1cfY9"
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&amp;destination=28.7048389,80.5740302"
UPDATED = "18 November 2026"

CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self'; "
       "img-src 'self' data:; frame-src https://maps.google.com https://www.google.com; "
       "base-uri 'none'; form-action 'none'; upgrade-insecure-requests")

ICON = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3Z"/><path d="M9 3v15M15 6v15"/></svg>',
 "watch": '<svg viewBox="0 0 48 48" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="16" y="3" width="16" height="9" rx="2"/><rect x="16" y="36" width="16" height="9" rx="2"/><circle cx="24" cy="24" r="13"/><path d="M24 17v7l5 3"/></svg>',
 "tool": '<svg viewBox="0 0 48 48" fill="none" stroke="#C9D6E8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="24" cy="24" r="13"/><path d="M24 11v4M24 33v4M11 24h4M33 24h4"/><path d="m31 9 8 8-6 6-8-8Z"/></svg>',
}

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><circle cx="16" cy="16" r="15" fill="#FFFFFF"/>'
        '<circle cx="16" cy="16" r="12" fill="#9B2D20"/><path d="M16 9v7l4.5 3" stroke="#FFFFFF" stroke-width="2.6" '
        'stroke-linecap="round" fill="none"/></svg>')

def head(title, desc, path, root=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}{path}">
<meta name="theme-color" content="#1034A6">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/style.css">
<script src="{root}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{root or './'}" aria-label="Deepak Watch Center, home">{LOGO}<span>Deepak <b>Watch</b> Center</span></a>
    <nav class="nav" aria-label="Main">
      <button class="menu-toggle" id="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <ul id="menu">
        <li><a href="{root or './'}#about">About</a></li>
        <li><a href="{root or './'}#services">Services</a></li>
        <li><a href="{root or './'}#visit">Visit us</a></li>
        <li><a class="call" href="tel:{TEL_M}">Call {PHONE_M}</a></li>
      </ul>
    </nav>
  </div>
</header>
"""

FOOT = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <h2>Deepak Watch Center</h2>
        <p>New watches with warranty and repairs for almost every kind of watch, in Dhangadhi for over 30 years.</p>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li>{ADDRESS}</li>
          <li>Mobile: <a href="tel:{TEL_M}">{PHONE_M}</a></li>
          <li>Phone: <a href="tel:{TEL_L}">{PHONE_L}</a></li>
        </ul>
      </div>
      <div>
        <h2>Pages</h2>
        <ul>
          <li><a href="./#services">Services</a></li>
          <li><a href="./#visit">Visit us</a></li>
          <li><a href="privacy.html">Privacy and cookie policy</a></li>
          <li><a href="terms.html">Terms and conditions</a></li>
        </ul>
      </div>
    </div>
    <div class="fine"><span>© <span id="year">2026</span> Deepak Watch Center, Dhangadhi</span><span>This site uses no cookies and no tracking.</span></div>
  </div>
</footer>
</body>
</html>
"""

CLOCK = """<svg class="clock" viewBox="0 0 400 400" role="img" aria-labelledby="clock-t">
  <title id="clock-t">Illustration of a watch face showing the current time in Nepal</title>
  <circle cx="200" cy="200" r="190" fill="#0B1A40"/>
  <circle cx="200" cy="200" r="168" fill="none" stroke="#2B3F73" stroke-width="2"/>
  <g id="ticks" stroke="#FFFFFF" stroke-linecap="round">
    __TICKS__
  </g>
  <g font-family="Archivo, Arial, sans-serif" font-weight="800" font-size="30" fill="#FFFFFF" text-anchor="middle">
    <text x="200" y="88">12</text><text x="318" y="210">3</text><text x="200" y="332">6</text><text x="82" y="210">9</text>
  </g>
  <text x="200" y="140" font-family="Manrope, Arial, sans-serif" font-weight="700" font-size="13" letter-spacing="3" fill="#C9D6E8" text-anchor="middle">DHANGADHI</text>
  <line id="hand-h" x1="200" y1="214" x2="200" y2="118" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" transform="rotate(305 200 200)"/>
  <line id="hand-m" x1="200" y1="220" x2="200" y2="78" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" transform="rotate(60 200 200)"/>
  <line id="hand-s" x1="200" y1="232" x2="200" y2="66" stroke="#E2543F" stroke-width="2.5" stroke-linecap="round" transform="rotate(0 200 200)"/>
  <circle cx="200" cy="200" r="9" fill="#E2543F"/><circle cx="200" cy="200" r="3.5" fill="#0B1A40"/>
</svg>"""
import math
ticks = []
for i in range(60):
    a = math.radians(i * 6)
    r1 = 168 - (16 if i % 5 == 0 else 7)
    w = 4 if i % 5 == 0 else 1.6
    x1, y1 = 200 + r1 * math.sin(a), 200 - r1 * math.cos(a)
    x2, y2 = 200 + 162 * math.sin(a), 200 - 162 * math.cos(a)
    ticks.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="{w}"/>')
CLOCK = CLOCK.replace("__TICKS__", "\n    ".join(ticks))

INDEX = head("Deepak Watch Center | Watches and watch repair in Dhangadhi",
             "Deepak Watch Center on Bus Park Road, Dhangadhi: new watches with warranty and repairs for almost all types of watches, for over 30 years.", "/") + f"""
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-text">
      <p class="eyebrow">Bus Park Road, Dhangadhi</p>
      <h1 id="hero-title">Deepak Watch Center</h1>
      <p class="lead">New watches with warranty, and repairs for almost every kind of watch, from modern designs to vintage classics. Trusted in Dhangadhi for over 30 years.</p>
      <div class="actions">
        <a class="btn btn-red" href="tel:{TEL_M}">{ICON['phone']}Call {PHONE_M}</a>
        <a class="btn btn-ghost" href="{DIRECTIONS}" rel="noopener noreferrer" target="_blank">{ICON['pin']}Get directions<span class="sr-only"> (opens Google Maps in a new tab)</span></a>
      </div>
    </div>
    <div class="hero-art">
      {CLOCK}
      <p class="years">30+<small>years in Dhangadhi</small></p>
    </div>
  </section>

  <section class="strip" aria-label="Highlights">
    <ul class="wrap">
      <li><b>30+ years</b><span>serving Dhangadhi</span></li>
      <li><b>Warranty</b><span>on every new watch</span></li>
      <li><b>All types</b><span>of watches repaired</span></li>
      <li><b>4.4 / 5</b><span>on Google, 7 reviews</span></li>
    </ul>
  </section>

  <section class="block" id="about" aria-labelledby="about-title">
    <div class="wrap two">
      <div>
        <p class="sec-label">About us</p>
        <h2 id="about-title">Dhangadhi's watch shop for over 30 years</h2>
      </div>
      <div class="about-text">
        <p>Deepak Watch Center has been part of Dhangadhi for more than three decades, selling watches and repairing them for local customers.</p>
        <p>We sell a wide selection of quality watches, and every one is backed by a warranty. We also repair almost all types of watches, from modern designs to vintage classics.</p>
        <p>Our focus is on precision, good craftsmanship and happy customers. You will find us on Bus Park Road, Dhangadhi.</p>
      </div>
    </div>
  </section>

  <section class="block on-stone" id="services" aria-labelledby="services-title">
    <div class="wrap">
      <p class="sec-label">What we do</p>
      <h2 id="services-title">Our services</h2>
      <p class="intro">Two things, done well for over 30 years: selling good watches and keeping them running.</p>
      <div class="services">
        <article class="service">
          {ICON['watch']}
          <h3>New watches</h3>
          <p>Choose from a wide selection of quality watches in the shop.</p>
          <ul>
            <li>A warranty on every watch we sell</li>
            <li>See and try watches in the shop</li>
            <li>Call ahead to ask if a model is in stock</li>
          </ul>
        </article>
        <article class="service">
          {ICON['tool']}
          <h3>Watch repair</h3>
          <p>We repair almost all types of watches, old and new.</p>
          <ul>
            <li>Modern watches and vintage classics</li>
            <li>Bring your watch in and we will check it</li>
            <li>The cost is agreed with you before work starts</li>
          </ul>
        </article>
      </div>
      <p class="note">Questions about a watch or a repair? Call <a href="tel:{TEL_M}">{PHONE_M}</a>.</p>
    </div>
  </section>

  <section class="block" id="repairs" aria-labelledby="repairs-title">
    <div class="wrap">
      <p class="sec-label">Repairs</p>
      <h2 id="repairs-title">How a repair works</h2>
      <ol class="steps">
        <li><h3>Bring it in</h3><p>Visit the shop on Bus Park Road with your watch.</p></li>
        <li><h3>We check it</h3><p>We look at the watch, tell you what needs fixing, and agree the cost and time with you.</p></li>
        <li><h3>Pick it up</h3><p>Collect your watch from the shop when it is ready.</p></li>
      </ol>
    </div>
  </section>

  <section class="block on-stone" id="reviews" aria-labelledby="reviews-title">
    <div class="wrap">
      <p class="sec-label">Reviews</p>
      <h2 id="reviews-title">What customers say</h2>
      <div class="rating">
        <p class="score" aria-hidden="true">4.4</p>
        <div>
          <div class="stars" aria-hidden="true"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 3 6.6 7 .7-5.3 4.8 1.6 7L12 17.5 5.7 21.1l1.6-7L2 9.3l7-.7Z" fill="#9B2D20" stroke="#0B1A40" stroke-width="1.2"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 3 6.6 7 .7-5.3 4.8 1.6 7L12 17.5 5.7 21.1l1.6-7L2 9.3l7-.7Z" fill="#9B2D20" stroke="#0B1A40" stroke-width="1.2"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 3 6.6 7 .7-5.3 4.8 1.6 7L12 17.5 5.7 21.1l1.6-7L2 9.3l7-.7Z" fill="#9B2D20" stroke="#0B1A40" stroke-width="1.2"/></svg><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 3 6.6 7 .7-5.3 4.8 1.6 7L12 17.5 5.7 21.1l1.6-7L2 9.3l7-.7Z" fill="#9B2D20" stroke="#0B1A40" stroke-width="1.2"/></svg></div>
          <p>Rated 4.4 out of 5 by 7 customers on Google (November 2026). Read the reviews, or leave your own after your visit.</p>
          <div class="actions">
            <a class="btn btn-red" href="{MAPS}" rel="noopener noreferrer" target="_blank">Read reviews on Google<span class="sr-only"> (opens in a new tab)</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="block" id="faq" aria-labelledby="faq-title">
    <div class="wrap">
      <p class="sec-label">Questions</p>
      <h2 id="faq-title">Common questions</h2>
      <div class="faq">
        <details><summary>Do new watches come with a warranty?</summary><p>Yes. Every new watch we sell comes with a warranty. The terms depend on the watch and are explained when you buy it.</p></details>
        <details><summary>Can you repair old or vintage watches?</summary><p>Yes. We repair almost all types of watches, from modern designs to vintage classics. Bring the watch to the shop and we will check it.</p></details>
        <details><summary>Where is the shop?</summary><p>On Bus Park Road, Dhangadhi, Kailali. On Google Maps, search for "Deepak Watch Center" or use the Plus Code PH3F+WJ Dhangadhi.</p></details>
        <details><summary>When are you open?</summary><p>Please check our <a href="{MAPS}" rel="noopener noreferrer" target="_blank">Google Maps listing<span class="sr-only"> (opens in a new tab)</span></a> for today's hours, or call <a href="tel:{TEL_M}">{PHONE_M}</a>.</p></details>
        <details><summary>Can I check whether a watch is in stock?</summary><p>Yes. Call <a href="tel:{TEL_M}">{PHONE_M}</a> or <a href="tel:{TEL_L}">{PHONE_L}</a> before you visit.</p></details>
      </div>
    </div>
  </section>

  <section class="block on-stone" id="visit" aria-labelledby="visit-title">
    <div class="wrap">
      <p class="sec-label">Visit us</p>
      <h2 id="visit-title">Find the shop</h2>
      <div class="visit-grid">
        <div>
          <ul class="contact-list">
            <li><span class="ic">{ICON['pin']}</span><div><small>Address</small><b>{ADDRESS}</b><br><small>Plus Code: PH3F+WJ Dhangadhi</small></div></li>
            <li><span class="ic">{ICON['phone']}</span><div><small>Mobile</small><a href="tel:{TEL_M}">{PHONE_M}</a></div></li>
            <li><span class="ic">{ICON['phone']}</span><div><small>Landline</small><a href="tel:{TEL_L}">{PHONE_L}</a></div></li>
          </ul>
          <div class="actions">
            <a class="btn btn-red" href="{DIRECTIONS}" rel="noopener noreferrer" target="_blank">{ICON['arrow']}Get directions<span class="sr-only"> (opens Google Maps in a new tab)</span></a>
          </div>
        </div>
        <div class="map" id="map">
          <div class="map-consent">
            {ICON['map']}
            <p>The map is provided by Google. Loading it connects your browser to Google, which may set cookies. See our <a href="privacy.html#map">privacy policy</a>.</p>
            <button class="btn btn-red" id="load-map" type="button">Show map</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
""" + FOOT

PRIVACY = head("Privacy and cookie policy | Deepak Watch Center",
               "How the Deepak Watch Center website handles your information and cookies.", "/privacy.html") + f"""
<main id="main" class="legal">
  <div class="wrap">
    <h1>Privacy and cookie policy</h1>
    <p class="updated">Last updated: {UPDATED}</p>

    <h2>Who we are</h2>
    <p>This website belongs to Deepak Watch Center, {ADDRESS}. You can contact us about privacy on <a href="tel:{TEL_M}">{PHONE_M}</a> or <a href="tel:{TEL_L}">{PHONE_L}</a>.</p>

    <h2>What we collect</h2>
    <p>This website does not collect personal information. It has no contact form, no account sign-up, no newsletter and no online shop.</p>
    <p>If you call us, we use your number only to answer you. We do not sell or share it.</p>

    <h2>Cookies</h2>
    <p>This website does not set any cookies and does not use analytics or advertising trackers. Because of this, we do not show a cookie banner.</p>

    <h2 id="map">Google Maps</h2>
    <p>The map on our home page is provided by Google. It does not load until you press "Show map". When you do, your browser connects to Google, which may collect information such as your IP address and set its own cookies, under <a href="https://policies.google.com/privacy" rel="noopener noreferrer" target="_blank">Google's privacy policy<span class="sr-only"> (opens in a new tab)</span></a>. The "Get directions" button opens Google Maps directly.</p>

    <h2>Hosting and server logs</h2>
    <p>Like every website, our hosting provider receives basic technical information when you visit, such as your IP address, browser type and the page requested. This is used to deliver the site and protect it from abuse. We do not use it to identify you.</p>

    <h2>Fonts</h2>
    <p>Our fonts are stored on our own server, so loading the site does not contact Google Fonts or other font services.</p>

    <h2>Your rights</h2>
    <p>Under Nepal's Individual Privacy Act, 2075 (2018), you can ask us what information we hold about you and ask us to correct or delete it. Contact us using the details above.</p>

    <h2>Changes</h2>
    <p>If we change this policy, we will update the date at the top of this page.</p>
  </div>
</main>
""" + FOOT

TERMS = head("Terms and conditions | Deepak Watch Center",
             "Terms for using the Deepak Watch Center website.", "/terms.html") + f"""
<main id="main" class="legal">
  <div class="wrap">
    <h1>Terms and conditions</h1>
    <p class="updated">Last updated: {UPDATED}</p>

    <h2>About this website</h2>
    <p>This website gives information about Deepak Watch Center, {ADDRESS}. By using it, you agree to these terms.</p>

    <h2>Information on the site</h2>
    <p>We try to keep the information here correct and up to date. Products, prices and opening hours can change, so please call us before you visit if something is important to you. Nothing on this website is an offer to sell a specific product.</p>

    <h2>Purchases, warranty and repairs</h2>
    <p>All sales and repairs take place in our shop. Warranty terms depend on the watch and are explained at the time of purchase. Repair costs and timings are agreed with you in the shop before work starts.</p>

    <h2>Links to other websites</h2>
    <p>Some links, such as Google Maps, take you to other websites. We are not responsible for their content or privacy practices.</p>

    <h2>Copyright</h2>
    <p>The text, design and illustrations on this website belong to Deepak Watch Center. Please do not copy them without permission. Brand names of watches belong to their owners.</p>

    <h2>Liability</h2>
    <p>We are not liable for any loss caused by relying on information on this website. This does not limit any rights you have under Nepali law as a customer.</p>

    <h2>Law</h2>
    <p>These terms are governed by the laws of Nepal.</p>

    <h2>Contact</h2>
    <p>Questions about these terms: call <a href="tel:{TEL_M}">{PHONE_M}</a> or <a href="tel:{TEL_L}">{PHONE_L}</a>.</p>
  </div>
</main>
""" + FOOT

NOTFOUND = head("Page not found | Deepak Watch Center", "This page could not be found.", "/404.html", root="/") + f"""
<main id="main" class="legal">
  <div class="wrap">
    <h1>Page not found</h1>
    <p class="updated">Sorry, this page does not exist.</p>
    <p><a class="btn btn-red" href="/">Go to the home page</a></p>
  </div>
</main>
""" + FOOT

for name, html in (("index.html", INDEX), ("privacy.html", PRIVACY), ("terms.html", TERMS), ("404.html", NOTFOUND)):
    with open(name, "w") as f:
        f.write(html)
print("built")
