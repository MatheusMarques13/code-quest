// Edge Function: cria contas de aluno/tutor com service role (pré-confirmadas).
// Autorização: o 1º tutor pode ser criado sem auth (bootstrap); depois,
// criar tutor ou aluno exige um tutor autenticado.
import { createClient } from "jsr:@supabase/supabase-js@2";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

function json(obj: unknown, status = 200): Response {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders });
  if (req.method !== "POST") return json({ error: "method not allowed" }, 405);

  try {
    const url = Deno.env.get("SUPABASE_URL")!;
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
    const admin = createClient(url, serviceKey, {
      auth: { autoRefreshToken: false, persistSession: false },
    });

    const body = await req.json().catch(() => ({}));
    const email = String(body.email || "").trim().toLowerCase();
    const password = String(body.password || "");
    const display_name = String(body.display_name || "").trim();
    const role = body.role === "tutor" ? "tutor" : "student";
    if (!email || password.length < 6) {
      return json({ error: "email e senha (min 6) obrigatorios" }, 400);
    }

    const { count: tutorCount, error: cErr } = await admin
      .from("profiles").select("id", { count: "exact", head: true }).eq("role", "tutor");
    if (cErr) return json({ error: cErr.message }, 500);

    let callerIsTutor = false;
    const token = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "").trim();
    if (token) {
      const { data: ud } = await admin.auth.getUser(token);
      if (ud?.user) {
        const { data: prof } = await admin.from("profiles").select("role").eq("id", ud.user.id).single();
        callerIsTutor = prof?.role === "tutor";
      }
    }

    const bootstrap = (tutorCount ?? 0) === 0;
    if (role === "tutor") {
      if (!bootstrap && !callerIsTutor) return json({ error: "apenas tutor pode criar tutor" }, 403);
    } else {
      if (!callerIsTutor) return json({ error: "apenas tutor pode criar aluno" }, 403);
    }

    const { data: created, error: cuErr } = await admin.auth.admin.createUser({
      email,
      password,
      email_confirm: true,
      user_metadata: { display_name, role },
    });
    if (cuErr) return json({ error: cuErr.message }, 400);

    return json({ ok: true, user_id: created.user?.id, email, role, display_name });
  } catch (e) {
    return json({ error: String((e as Error)?.message || e) }, 500);
  }
});
