from flask import Flask, render_template, request

app = Flask(__name__)


answer, equation = 0, ""


@app.route("/", methods=["GET", "POST"])
def index():
    global answer, equation

    if request.method == "POST":
        symbol = request.form["symbol"]
        print("[SERVER]: got symbol:", symbol)
        match symbol:
            case "del_all":    # Clear the calculator
                equation, symbol = "", ""
            case "del_one":    # Deleting last symbol on calculator
                equation = equation[:-1]
                symbol = ""
            case "=":
                # Checking the correctness of a mathematical expression
                if equation != "" and equation[0].isdigit() and equation[-1].isdigit():
                    answer = eval(equation)
                symbol = ""

        if equation == "":  # Reset a variable of answer to its original form if there is no mathematical expression
            answer = 0

        equation = equation + symbol
    return render_template("index.html",
                           equation=equation,
                           answer=answer
                           )


if __name__ == '__main__':
    app.run(debug=False)
