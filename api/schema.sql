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
