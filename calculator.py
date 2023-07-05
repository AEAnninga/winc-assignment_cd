from flask import Flask, render_template, request, url_for
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
from util import calculate_input

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def calculator(result=None):
    if request.method == "POST":
        first_number = request.form['first-number']
        second_number = request.form['second-number']
        arithmetic_operator = request.form['arithmetic-operator']
        calculation_result = calculate_input(number_one=first_number,number_two=second_number,operator=arithmetic_operator)
        return render_template("index.html", result=calculation_result)

    if request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)