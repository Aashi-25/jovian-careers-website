from flask import Flask , render_template , jsonify , request
from database import init_db , load_jobs_from_db , load_jobs_by_id , add_application_to_db


app = Flask(__name__) #creates the flask app but doesn't run it

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Software Engineer',
#         'location': 'Bangalore, India',
#         'salary': '₹15,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Analyst',
#         'location': 'Delhi, India',
#         'salary': '₹8,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Frontend Developer',
#         'location': 'Punjab, India',
#         # 'salary': '₹12,00,000'
#     },
#     {
#         'id': 4,
#         'title': 'Machine Learning Engineer',
#         'location': 'Mumbai, India',
#         'salary': '₹18,00,000'
#     }
# ]

init_db(app)

@app.route("/") #registered a route for flask application
def hello_world():
    jobs_list = load_jobs_from_db()
    return render_template('home.html' , jobs = jobs_list ,  company_name = 'Jovian')

@app.route("/api/jobs") #json endpoint
def list_jobs():
    return jsonify(load_jobs_from_db())

@app.route("/job/<id>")
def show_job(id):
    job = load_jobs_by_id(id)
    if not job:
        return "Not Found" , 404
    return render_template('jobpage.html' , job = job)

@app.route("/api/job/<id>")
def show_job_json(id):
    job = load_jobs_by_id(id)
    return jsonify(job)

@app.route("/job/<id>/apply" , methods=['post'])
def apply_to_job(id):

    # store this in db (done)
    # send an email
    # display an acknowledgement

    data = request.form
    add_application_to_db(id , data)
    job = load_jobs_by_id(id)
    return render_template('application_submitted.html' , application = data , job = job)

if __name__ == '__main__':
    app.run(debug = True)