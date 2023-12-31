from flask import Flask, jsonify, render_template, request

from database import load_job_from_db, load_jobs_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_speedy():
  jobs = load_jobs_from_db()
  return render_template("home.html", 
                         jobs=jobs)

@app.route("/api/jobs")
def job_list():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found", 404
  return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=['post'])
def applicant_data(id):
  data = request.form
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  
  return render_template("appsubmitted.html", application = data, job = job)
  
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)