// Cliente Supabase compartilhado.
// A chave "publishable/anon" é segura no navegador — o acesso é protegido por Row Level Security (RLS) no banco.
(function () {
  var SUPABASE_URL = 'https://pqytpynhhknigmncgufx.supabase.co';
  var SUPABASE_KEY = 'sb_publishable_9oL2aAxCVW3AtGmV1SnhnQ_2e7NP6tC';
  if (!window.supabase || !window.supabase.createClient) {
    console.error('[code-quest] supabase-js não carregou antes de js/supabase.js');
    return;
  }
  window.sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
})();
