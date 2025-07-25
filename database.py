from flask import has_app_context
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


db = SQLAlchemy()

def init_db(app):
    """Bind SQLAlchemy to the passed Flask app and configure it."""
    app.config.setdefault(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://postgres:goel_aashi_25@db.djoowctsfbugwodshmas.supabase.co:5432/postgres"
    )
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    db.init_app(app)

def load_jobs_from_db():
    """Return all jobs as a list[dict]. Must be called inside an app/request context."""
    if not has_app_context():
        raise RuntimeError("load_jobs_from_db() must be called inside an app context")
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        return [dict(row._mapping) for row in result]

