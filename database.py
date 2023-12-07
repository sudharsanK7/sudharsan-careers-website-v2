import os

from sqlalchemy import create_engine, text


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

def add_application_to_db(job_id, data):
  try:
      with engine.connect() as conn:
          query = text('INSERT into applications (job_id, full_name, email, linkedin_url, '
                         'education, work_experience, resume_url) VALUES '
                         '(:job_id, :full_name, :email, :linkedin_url, :education, '
                         ':work_experience, :resume_url)')

          conn.execute(query, 
                         {
                             'job_id': job_id,  
                             'full_name': data['full_name'],  
                             'email': data['email'], 
                             'linkedin_url': data['linkedin_url'],  
                             'education': data['education'],  
                             'work_experience': data['work_experience'], 
                             'resume_url': data['resume_url']  
                         })

            # Add a commit statement
          conn.commit()
  except Exception as e:
        print(f"Error adding application to the database: {e}")