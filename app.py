from flask import Flask

app = Flask(__name__) #creates the flask app but doesn't run it

@app.route("/") #registered a route for flask application
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)