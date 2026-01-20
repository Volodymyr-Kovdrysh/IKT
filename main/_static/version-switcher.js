(function () {
  function detectVersionFromPath() {
    const p = window.location.pathname;
    // ловимо /.../v2009.3/... або /.../main/ або /.../latest/
    const m = p.match(/\/(latest|main|v\d+(?:\.\d+)+)\//);
    return m ? m[1] : null;
  }

  function applyActiveVersion() {
    const current = detectVersionFromPath();
    if (!current) return false;

    const btn = document.querySelector(".version-switcher__button");
    const menu = document.querySelector(".version-switcher__menu");
    if (!btn || !menu) return false;

    // меню вже має бути заповнене <a data-version-name="...">
    const items = menu.querySelectorAll('a[data-version-name]');
    if (!items.length) return false;

    // знайти пункт поточної версії
    const target = menu.querySelector(`a[data-version-name="${current}"]`);
    if (!target) return false;

    // 1) кнопка
    btn.textContent = current;
    btn.dataset.activeVersionName = current;
    btn.dataset.activeVersion = current;

    // 2) active клас у списку
    items.forEach(a => {
      const isActive = a.dataset.versionName === current;
      a.classList.toggle("active", isActive);
      a.setAttribute("aria-selected", isActive ? "true" : "false");
    });

    return true;
  }

  // pydata заповнює меню “на load”, тому робимо кілька спроб
  window.addEventListener("load", () => {
    let tries = 0;
    const t = setInterval(() => {
      tries += 1;
      if (applyActiveVersion() || tries >= 30) clearInterval(t); // ~3 секунди
    }, 100);
  });
})();

