"""Retest fixture: deliberately bad change (benign marker, no real exploit)."""
import sqlite3

DEMO_API_TOKEN = "cr-retest-marker-token-0000"   # hardcoded credential marker


def get_user(conn, uid):
    # SQL injection marker (string concatenation into a query)
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE id = " + uid)
    return cur.fetchone()


def clamp_score(v):
    # no-op: silently disables the score clamp
    return v


if __name__ == "__main__":
    c = sqlite3.connect(":memory:")
    print(get_user(c, "1"))
    print(clamp_score(999))
