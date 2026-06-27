# Basic Flask application
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)  # create an instance of flask class as app


@app.route("/")      # dedcorator to define route           
def Welcome():                      
    return " Welcome to my page"


# @app.route('/success/<int:score>')
# def success(score):
#     res = ""
#     if(score > 50):
#         res = "Pass"
#     else:
#         res = "Fail"
    
#     return render_template('result.html', results = res)



@app.route('/success/<float:score>')
def success(score):
    res = ""
    if(score > 50):
        res = "Pass"
    else:
        res = "Fail"
    
    res = {'score' : score, 'results' : res}
    
    return render_template('result1.html', results = res)


@app.route('/submit', methods = ['POST', 'GET'])
def getresults():
    total_score = 0

    if request.method == 'GET':
        return render_template('getResults.html')

    if request.method == 'POST':
        s1 = float(request.form['sub1'])
        s2 = float(request.form['sub2'])
        s3 = float(request.form['sub3'])
        s4 = float(request.form['sub4'])

        total_score = (s1 + s2 + s3 + s4) / 4
    # else:
    #     return render_template('getResults.html')

    return redirect(url_for('success', score=total_score))


if __name__ == "__main__": # check if the script run directely
    app.run(debug = True)  # runs the app