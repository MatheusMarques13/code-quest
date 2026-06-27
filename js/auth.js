// Helpers de autenticação (Supabase Auth).
window.cqAuth = {
  async signIn(email, password) {
    return await window.sb.auth.signInWithPassword({
      email: String(email || '').trim().toLowerCase(),
      password: password
    });
  },
  async signOut() {
    try { await window.sb.auth.signOut(); } catch (e) {}
  },
  async getSession() {
    const { data } = await window.sb.auth.getSession();
    return data ? data.session : null;
  },
  async getUser() {
    const { data } = await window.sb.auth.getUser();
    return data ? data.user : null;
  },
  async getProfile() {
    const u = await this.getUser();
    if (!u) return null;
    const { data, error } = await window.sb
      .from('profiles').select('*').eq('id', u.id).single();
    if (error) { console.warn('[code-quest] getProfile', error.message); return null; }
    return data;
  }
};
