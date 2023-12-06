from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_speedy():
  jobs = load_jobs_from_db()
  return render_template("home.html", 
                         jobs=jobs, 
                         company_name = "Speedy")

@app.route("/api/jobs")
def job_list():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)