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
  const photoLinks = [...document.querySelectorAll('.case-figure a')];
  if (photoLinks.length && typeof HTMLDialogElement !== 'undefined') {
    const dialog = document.createElement('dialog');
    dialog.className = 'photo-dialog';
    dialog.setAttribute('aria-label', 'Visionneuse des visuels');
    dialog.innerHTML = `
      <div class="photo-stage">
        <div class="photo-toolbar">
          <span class="photo-count"></span>
          <a class="photo-original" href="#" target="_blank" rel="noopener" aria-label="Ouvrir l'image originale pour zoomer">Zoom HD ↗</a>
          <button type="button" class="photo-close" aria-label="Fermer la photo">Fermer ×</button>
        </div>
        <span class="photo-announcement sr-only" aria-live="polite" aria-atomic="true"></span>
        <img class="photo-full" alt="">
        <div class="photo-controls">
          <button type="button" class="photo-prev" aria-label="Photo précédente">←</button>
          <p class="photo-caption" aria-hidden="true"></p>
          <button type="button" class="photo-next" aria-label="Photo suivante">→</button>
        </div>
      </div>`;
    document.body.append(dialog);
    const image = dialog.querySelector('.photo-full');
    const caption = dialog.querySelector('.photo-caption');
    const counter = dialog.querySelector('.photo-count');
    const original = dialog.querySelector('.photo-original');
    const announcement = dialog.querySelector('.photo-announcement');
    const previous = dialog.querySelector('.photo-prev');
    const next = dialog.querySelector('.photo-next');
    const closeButton = dialog.querySelector('.photo-close');
    let current = 0;
    let opener = null;
    const display = index => {
      current = index;
      const link = photoLinks[index];
      const description = link.querySelector('img').alt;
      image.src = link.href;
      image.alt = description;
      caption.textContent = description;
      counter.textContent = `${index + 1} / ${photoLinks.length}`;
      original.href = link.href;
      announcement.textContent = `Photo ${index + 1} sur ${photoLinks.length} : ${description}`;
      previous.disabled = index === 0;
      next.disabled = index === photoLinks.length - 1;
    };
    photoLinks.forEach((link, index) => link.addEventListener('click', event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      display(index);
      dialog.showModal();
      closeButton.focus();
    }));
    previous.addEventListener('click', () => display(current - 1));
    next.addEventListener('click', () => display(current + 1));
    closeButton.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener('close', () => opener?.focus());
    dialog.addEventListener('keydown', event => {
      if (event.key === 'ArrowRight' && !next.disabled) {
        event.preventDefault();
        display(current + 1);
      } else if (event.key === 'ArrowLeft' && !previous.disabled) {
        event.preventDefault();
        display(current - 1);
      }
    });
  }
  document.documentElement.classList.add('js-ready');
})();
