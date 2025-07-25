from flask import Flask , render_template , jsonify
from database import init_db , load_jobs_from_db


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
    return jsonify(load_jobs_from_db)

if __name__ == '__main__':
    app.run(debug = True)