/*
 * Workshop progress API — https://workshops-api.casabe.studio
 *
 *   POST /v1/progress   an attendee's page saves their name and ticked steps.
 *                       No login: the attendee is a random id their phone keeps.
 *   GET  /v1/progress   the instructor's progress page reads everyone. Open by
 *                       choice: names and ticks are not treated as private.
 *   POST /v1/progress/clear    hide everyone from the progress page (between
 *                              workshops). Nothing is deleted, so it can be undone.
 *   POST /v1/progress/restore  undo the most recent clear.
 *
 * Storage is one D1 table (schema.sql), one row per attendee per workshop.
 */

// Workshops this API accepts, and how many steps each has.
const WORKSHOPS = { "canvas-pouch": 19 };

const MAX_BODY_BYTES = 4096;
const MAX_NAME = 60;
const PARTICIPANT_ID = /^[A-Za-z0-9-]{16,64}$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const cors = corsHeaders(request.headers.get("Origin"), env);

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    try {
      if (url.pathname === "/v1/progress") {
        if (request.method === "POST") return await save(request, env, cors);
        if (request.method === "GET") return await list(url, env, cors);
        return json({ error: "Use GET or POST" }, 405, cors);
      }
      if (url.pathname === "/v1/progress/clear" && request.method === "POST") return await clearList(request, env, cors);
      if (url.pathname === "/v1/progress/restore" && request.method === "POST") return await restoreList(request, env, cors);
      return json({ error: "Not found" }, 404, cors);
    } catch (err) {
      console.error(err);
      return json({ error: "Something went wrong saving progress. Try again." }, 500, cors);
    }
  },
};

async function save(request, env, cors) {
  const raw = await request.text();
  if (raw.length > MAX_BODY_BYTES) return json({ error: "Request too large" }, 413, cors);

  let body;
  try { body = JSON.parse(raw); } catch { return json({ error: "Body must be JSON" }, 400, cors); }

  const workshop = String(body.workshop || "");
  const total = WORKSHOPS[workshop];
  if (!total) return json({ error: "Unknown workshop" }, 400, cors);

  const participant = String(body.participant || "");
  if (!PARTICIPANT_ID.test(participant)) return json({ error: "Missing or malformed participant id" }, 400, cors);

  const name = String(body.name || "").replace(/\s+/g, " ").trim().slice(0, MAX_NAME);
  if (!name) return json({ error: "Add a name first" }, 400, cors);

  if (!Array.isArray(body.done)) return json({ error: "done must be a list of step numbers" }, 400, cors);
  const done = [...new Set(body.done.map(Number))]
    .filter((n) => Number.isInteger(n) && n >= 1 && n <= total)
    .sort((a, b) => a - b);

  const now = Date.now();
  await env.DB.prepare(
    `INSERT INTO progress (workshop, participant, name, done, total, created_at, updated_at)
     VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?6)
     ON CONFLICT (workshop, participant)
     DO UPDATE SET name = excluded.name, done = excluded.done, total = excluded.total, updated_at = excluded.updated_at`
  ).bind(workshop, participant, name, JSON.stringify(done), total, now).run();

  return json({ ok: true, saved_at: now }, 200, cors);
}

async function list(url, env, cors) {
  const workshop = url.searchParams.get("workshop") || "";
  if (!WORKSHOPS[workshop]) return json({ error: "Unknown workshop" }, 400, cors);

  const cleared = await latestClear(env, workshop);
  const { results } = await env.DB.prepare(
    `SELECT participant, name, done, total, created_at, updated_at
     FROM progress WHERE workshop = ?1 AND updated_at > ?2 ORDER BY updated_at DESC LIMIT 500`
  ).bind(workshop, cleared ? cleared.cleared_at : 0).all();

  const people = results.map((r) => ({ ...r, done: JSON.parse(r.done) }));
  return json({ workshop, total: WORKSHOPS[workshop], now: Date.now(), cleared_at: cleared ? cleared.cleared_at : null, people },
    200, { ...cors, "Cache-Control": "no-store" });
}

async function clearList(request, env, cors) {
  const workshop = await workshopFromBody(request);
  if (!workshop) return json({ error: "Unknown workshop" }, 400, cors);
  const now = Date.now();
  await env.DB.prepare("INSERT INTO clears (workshop, cleared_at) VALUES (?1, ?2)").bind(workshop, now).run();
  return json({ ok: true, cleared_at: now }, 200, cors);
}

async function restoreList(request, env, cors) {
  const workshop = await workshopFromBody(request);
  if (!workshop) return json({ error: "Unknown workshop" }, 400, cors);
  const cleared = await latestClear(env, workshop);
  if (!cleared) return json({ error: "There's no clear to undo" }, 409, cors);
  await env.DB.prepare("UPDATE clears SET undone = 1 WHERE id = ?1").bind(cleared.id).run();
  return json({ ok: true }, 200, cors);
}

function latestClear(env, workshop) {
  return env.DB.prepare(
    "SELECT id, cleared_at FROM clears WHERE workshop = ?1 AND undone = 0 ORDER BY cleared_at DESC, id DESC LIMIT 1"
  ).bind(workshop).first();
}

async function workshopFromBody(request) {
  const raw = await request.text();
  if (raw.length > MAX_BODY_BYTES) return null;
  try {
    const workshop = String(JSON.parse(raw).workshop || "");
    return WORKSHOPS[workshop] ? workshop : null;
  } catch { return null; }
}

function corsHeaders(origin, env) {
  const allowed = String(env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
  const headers = {
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
  if (origin && allowed.includes(origin)) headers["Access-Control-Allow-Origin"] = origin;
  return headers;
}

function json(data, status, headers) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...headers, "Content-Type": "application/json; charset=utf-8" },
  });
}
