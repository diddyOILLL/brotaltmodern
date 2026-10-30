'use strict';

// All content and navigation live in HTML. JavaScript adds small conveniences.
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.primary-nav');
const breadMenu = document.querySelector('.bread-menu');

if (menuButton && navigation) {
  document.documentElement.classList.add('nav-enabled');
  menuButton.hidden = false;
  const closeMenu = () => {
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.querySelector('.menu-label').textContent = 'Menü';
  };
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(expanded));
    navigation.classList.toggle('is-open', expanded);
    menuButton.querySelector('.menu-label').textContent = expanded ? 'Schließen' : 'Menü';
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    if (breadMenu?.open) {
      breadMenu.open = false;
      breadMenu.querySelector('summary').focus();
    } else if (navigation.classList.contains('is-open')) {
      closeMenu();
      menuButton.focus();
    }
  });
  document.addEventListener('click', event => {
    if (breadMenu?.open && !breadMenu.contains(event.target)) breadMenu.open = false;
    if (!event.target.closest('.site-header')) closeMenu();
  });
}

const filters = document.querySelector('.filters');
const cards = [...document.querySelectorAll('.bread-card')];
const resultCount = document.querySelector('.result-count');
if (filters && cards.length) {
  filters.hidden = false;
  filters.addEventListener('click', event => {
    const button = event.target.closest('[data-filter]');
    if (!button) return;
    filters.querySelectorAll('button').forEach(item => {
      item.setAttribute('aria-pressed', String(item === button));
    });
    let visible = 0;
    cards.forEach(card => {
      const match = button.dataset.filter === 'all' || card.dataset.category === button.dataset.filter;
      card.hidden = !match;
      if (match) visible += 1;
    });
    resultCount.textContent = `${visible} von 7 Brotsorten`;
  });
}

// Animate at entry, without hiding elements while they wait for the observer.
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-entering');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(element => observer.observe(element));
}
