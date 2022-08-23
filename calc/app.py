from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def show_add():
    """ return sum of a + b """
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route("/sub")
def show_sub():
    """ return difference of a - b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))


@app.route("/mult")
def show_mult():
    """ return product of a * b """
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))


@app.route("/div")
def show_div():
    """ return division of a / b """
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

# ----- PART 2 -----


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<calc>")
def math(calc):
    """ return result of a ? b """
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operators[calc](a, b)

    return str(result)
