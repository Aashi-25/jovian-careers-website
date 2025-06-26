from flask import Flask , render_template , jsonify

app = Flask(__name__) #creates the flask app but doesn't run it

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Bangalore, India',
        'salary': '₹15,00,000'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'Delhi, India',
        'salary': '₹8,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Punjab, India',
        # 'salary': '₹12,00,000'
    },
    {
        'id': 4,
        'title': 'Machine Learning Engineer',
        'location': 'Mumbai, India',
        'salary': '₹18,00,000'
    }
]

@app.route("/") #registered a route for flask application
def hello_world():
    return render_template('home.html' , jobs = JOBS ,  company_name = 'Jovian')

@app.route("/api/jobs") #json endpoint
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug = True)