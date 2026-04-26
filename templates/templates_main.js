// templates/templates_main.js
// Shared JavaScript for all pages

document.addEventListener('DOMContentLoaded', function () {

  // ── Navbar scroll effect ──────────────────
  var navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });
  }

  // ── Mobile nav toggle ─────────────────────
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('active');
      links.classList.toggle('open');
    });
  }

  // ── FAQ accordion ─────────────────────────
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('open'); });
      if (!wasOpen) item.classList.add('open');
    });
  });

  // ── Scroll-triggered animations ───────────
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('.observe-me').forEach(function (el) { observer.observe(el); });
  }

  // ── Smooth scroll ─────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

  // ── Card 3D tilt effect ──────────────────
  document.querySelectorAll('.resource-card').forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var rect = card.getBoundingClientRect();
      var x = (e.clientX - rect.left) / rect.width - 0.5;
      var y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = 'translateY(-8px) perspective(800px) rotateY(' + (x * 6) + 'deg) rotateX(' + (-y * 4) + 'deg)';
    });
    card.addEventListener('mouseleave', function () {
      card.style.transform = 'translateY(0) perspective(800px) rotateY(0) rotateX(0)';
    });
  });

  // ── Count-up animation ────────────────────
  function animateCount(el, target, suffix) {
    var start = 0;
    var duration = 1500;
    var startTime = null;
    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target) + (suffix || '');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  var statsObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var el = entry.target;
        var target = parseInt(el.dataset.count || '0', 10);
        var suffix = el.dataset.suffix || '';
        animateCount(el, target, suffix);
        statsObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-count]').forEach(function (el) { statsObserver.observe(el); });

  // ── Active nav link ───────────────────────
  var currentPath = window.location.pathname.replace(/\/$/, '');
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var href = a.getAttribute('href').replace(/\/$/, '');
    if (href === currentPath || (href && currentPath.endsWith(href))) {
      a.classList.add('active');
    }
  });
});
