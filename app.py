from flask import Flask, render_template, jsonify

from database import get_jobs

app = Flask(__name__)


@app.route("/")
def hello_jovian():
  JOBS=get_jobs()
  return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  JOBS=get_jobs()
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)