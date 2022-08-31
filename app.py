from flask import Flask, render_template, jsonify,request

from database import get_jobs,load_job_from_db,add_application_db

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  JOBS=get_jobs()
  return render_template('home.html', 
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  JOBS=get_jobs()
  return jsonify(JOBS)
@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job)

@app.route('/job/<id>/apply',methods=['post'])
def apply_to_job(id):
  data=request.form
  job=load_job_from_db(id)
  add_application_db(id,data)
  return render_template('application_submitted.html',application=data,job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)