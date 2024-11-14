"""
Flask Calculator API

This simple Flask application provides a REST API for performing basic arithmetic operations
(addition, subtraction, multiplication, and division) on two numbers.
"""

from flask import Flask, request


app = Flask(__name__)


@app.route('/calculate')
def calculate():
    """
    Performs the specified arithmetic operation on two numbers
    provided in the request query parameters.
    Supported operations:
      - sum (addition)
      - sub (subtraction)
      - mul (multiplication)
      - div (division)
    """

    op = request.args.get('op')
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op is None or arg1 is None or arg2 is None:
        return "Missing required parameters: op, arg1, and arg2", 400

    result = None

    if op == 'sum':
        result = arg1 + arg2
    elif op == 'sub':
        result = arg1 - arg2
    elif op == 'mul':
        result = arg1 * arg2
    elif op == 'div':
        if arg2 != 0:
            result = arg1 / arg2
        else:
            return "Division by zero is not allowed", 400
    else:
        return "Unknown operation", 400

    return f"{arg1} {op} {arg2} = {result}"


if __name__ == '__main__':
    app.run(debug=True)
