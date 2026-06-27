# Basic Flask application
from flask import Flask

app = Flask(__name__)  # create an instance of flask class as app


@app.route("/")      # dedcorator to define route           
def Welcome():                      
    return " Welcome to my page"


if __name__ == "__main__": # check if the script run directely
    app.run(debug = True)  # runs the app