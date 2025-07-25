from database import db , app
from sqlalchemy import text

with app.app_context():
    with db.engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        for row in result :
            print(row)