from sqlalchemy import create_engine, text

import os

from sqlalchemy.sql.selectable import ReturnsRows

db_connection_string = os.environ['DB_CONN_STR']

engine = create_engine(db_connection_string, 
                       connect_args={
                         "ssl": {
                           "ssl_ca": "ca.pem"
                         }
                       })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      return row[0]._asdict()
