(() => {
  'use strict';
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#nav');
  if (menu && nav) {
    const close = () => {
      menu.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-label', 'Ouvrir le menu');
      nav.classList.remove('open');
    };
    menu.addEventListener('click', () => {
      const isOpen = menu.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('aria-expanded', String(!isOpen));
      menu.setAttribute('aria-label', isOpen ? 'Ouvrir le menu' : 'Fermer le menu');
      nav.classList.toggle('open', !isOpen);
    });
    nav.addEventListener('click', event => {
      if (event.target.closest('a')) close();
    });
    document.addEventListener('click', event => {
      if (nav.classList.contains('open') && !nav.contains(event.target) && !menu.contains(event.target)) close();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
        close();
        menu.focus();
      }
    });
  }

  const buttons = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('.gallery-grid .project-card')];
  const count = document.querySelector('.result-count');
  const empty = document.querySelector('.empty');
  if (buttons.length && cards.length && count) {
    const apply = (selected, updateUrl) => {
      const button = buttons.find(item => item.dataset.filter === selected) || buttons[0];
      selected = button.dataset.filter;
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      let visible = 0;
      cards.forEach(card => {
        card.hidden = selected !== 'Tous' && card.dataset.category !== selected;
        // Décalage en quinconce calculé sur les cartes visibles, pas sur l'ordre du DOM.
        card.classList.toggle('is-offset', !card.hidden && visible++ % 2 === 1);
      });
      count.textContent = visible + (visible === 1 ? ' projet' : ' projets');
      if (empty) empty.hidden = visible !== 0;
      if (updateUrl) {
        const hash = selected === 'Tous' ? '' : '#filtre=' + encodeURIComponent(selected);
        history.replaceState(null, '', location.pathname + location.search + hash);
      }
    };
    const fromHash = () => {
      const match = location.hash.match(/^#filtre=(.+)$/);
      let value = 'Tous';
      if (match) { try { value = decodeURIComponent(match[1]); } catch (_) { /* hash invalide */ } }
      apply(value, false);
    };
    buttons.forEach(button => button.addEventListener('click', () => apply(button.dataset.filter, true)));
    window.addEventListener('hashchange', fromHash);
    fromHash();
  }
  document.documentElement.classList.add('js-ready');
})();
