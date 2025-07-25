import os
from flask import has_app_context
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    """Bind SQLAlchemy to the passed Flask app and configure it."""
    db_url = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

def load_jobs_from_db():
    """Return all jobs as a list[dict]. Must be called inside an app/request context."""
    if not has_app_context():
        raise RuntimeError("load_jobs_from_db() must be called inside an app context")
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        return [dict(row._mapping) for row in result]

def load_jobs_by_id(id):
    if not has_app_context():
        raise RuntimeError("load_jobs_by_id() must be called inside an app context")
    with db.engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),{"val" : id})
        row = result.fetchone()
        if row is None:
            return None
        return dict(row._mapping)