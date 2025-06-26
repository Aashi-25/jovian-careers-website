from flask import Flask , render_template

app = Flask(__name__) #creates the flask app but doesn't run it

@app.route("/") #registered a route for flask application
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)