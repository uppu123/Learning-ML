from flask import Flask, render_template

app = Flask(__name__)  # create an instance of flask class as app


@app.route("/home")      # dedcorator to define route           
def home():                      
    return render_template("home.html")


@app.route("/booking")      # dedcorator to define route           
def booking():                      
    return render_template("booking.html")                                   ## All the Html files are stored in templates and all css files are stored in static folder


@app.route("/listing")      # dedcorator to define route           
def listing():                      
    return render_template("listing.html")


if __name__ == "__main__": # check if the script run directely
    app.run(debug = True)  # runs the app