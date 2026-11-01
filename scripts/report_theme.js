(function() {
  var key = 'market-report-theme';
  var media = window.matchMedia('(prefers-color-scheme: dark)');

  function applyTheme(setting) {
    var actual = setting === 'auto' ? (media.matches ? 'dark' : 'light') : setting;
    document.documentElement.dataset.theme = actual;
    document.documentElement.dataset.themeSetting = setting;
    try { localStorage.setItem(key, setting); } catch (e) {}
    document.querySelectorAll('[data-theme-option]').forEach(function(btn) {
      btn.setAttribute('aria-pressed', btn.dataset.themeOption === setting ? 'true' : 'false');
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('table').forEach(function(table) {
      if (!table.parentElement.classList.contains('table-wrap')) {
        var wrap = document.createElement('div');
        wrap.className = 'table-wrap';
        table.parentNode.insertBefore(wrap, table);
        wrap.appendChild(table);
      }
    });
    var stored = 'auto';
    try { stored = localStorage.getItem(key) || 'auto'; } catch (e) {}
    applyTheme(stored);
    document.querySelectorAll('[data-theme-option]').forEach(function(btn) {
      btn.addEventListener('click', function() { applyTheme(this.dataset.themeOption); });
    });
  });

  media.addEventListener('change', function() {
    var stored = 'auto';
    try { stored = localStorage.getItem(key) || 'auto'; } catch (e) {}
    if (stored === 'auto') applyTheme('auto');
  });
})();
