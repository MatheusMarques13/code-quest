// Protege páginas que exigem login: se não há sessão, manda pro login.
(async function () {
  function kick() {
    document.documentElement.style.display = 'none';
    location.replace('landing.html');
  }
  try {
    if (!window.sb) return kick();
    const { data } = await window.sb.auth.getSession();
    if (!data || !data.session) kick();
  } catch (e) {
    kick();
  }
})();
