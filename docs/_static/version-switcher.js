(function () {
  function detectVersionFromPath() {
    const p = window.location.pathname;
    // ловимо /.../v2009/... або /.../v2009.3/... або /.../main/ або /.../latest/
    const m = p.match(/\/(latest|main|v\d+(?:\.\d+)*)\//);
    return m ? m[1] : null;
  }

  function applyActiveVersion() {
    const current = detectVersionFromPath();
    if (!current) return false;

    const btn = document.querySelector(".version-switcher__button");
    const menu = document.querySelector(".version-switcher__menu");
    if (!btn || !menu) return false;

    const items = menu.querySelectorAll('a[data-version]');
    if (!items.length) return false;

    const target = menu.querySelector(`a[data-version="${current}"]`);
    if (!target) return false;

    btn.textContent = current;
    btn.dataset.activeVersionName = current;
    btn.dataset.activeVersion = current;

    items.forEach(a => {
      const isActive = a.dataset.version === current;
      a.classList.toggle("active", isActive);
      a.setAttribute("aria-selected", isActive ? "true" : "false");
    });

    return true;
  }

  window.addEventListener("load", () => {
    let tries = 0;
    const t = setInterval(() => {
      tries += 1;
      if (applyActiveVersion() || tries >= 30) clearInterval(t);
    }, 100);
  });
})();

