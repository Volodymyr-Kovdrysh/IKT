(function () {
  const path = window.location.pathname;

  // витягаємо поточну версію з URL: /main/... або /v2009.1/...
  const m = path.match(/\/(main|v\d+\.\d+(?:\.\d+)?)\//);
  const current = m ? m[1] : "main";
console.log(m,current)
  const wrapper = document.querySelector(".version-switcher");
  const select = wrapper ? wrapper.querySelector("select") : null;
  if (!select) return;

  // виставляємо поточну версію в select
  for (const opt of select.options) {
    if (opt.text.trim() === current) {
      select.value = opt.value;
      break;
    }
  }

  // при зміні: замінюємо /current/ на /target/
  select.addEventListener("change", (e) => {
    const targetText = e.target.selectedOptions[0].text.trim();
    const next = path.replace(`/${current}/`, `/${targetText}/`);
    window.location.pathname = next;
  });
})();

