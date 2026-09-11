-- One row per attendee per workshop. `done` is a JSON list of ticked step numbers.
CREATE TABLE IF NOT EXISTS progress (
  workshop    TEXT    NOT NULL,
  participant TEXT    NOT NULL,
  name        TEXT    NOT NULL,
  done        TEXT    NOT NULL DEFAULT '[]',
  total       INTEGER NOT NULL,
  created_at  INTEGER NOT NULL,
  updated_at  INTEGER NOT NULL,
  PRIMARY KEY (workshop, participant)
);

-- "Clear list" on the progress page. Rows in `progress` are never deleted: the page
-- only shows people updated after the latest clear that hasn't been undone.
CREATE TABLE IF NOT EXISTS clears (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  workshop   TEXT    NOT NULL,
  cleared_at INTEGER NOT NULL,
  undone     INTEGER NOT NULL DEFAULT 0
);
