from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    history = []   # ✅ local history (resets every request)

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
                symbol = "+"
            elif operation == "sub":
                result = num1 - num2
                symbol = "-"
            elif operation == "mul":
                result = num1 * num2
                symbol = "*"
            elif operation == "div":
                result = num1 / num2
                symbol = "/"

            history.append(f"{num1} {symbol} {num2} = {result}")

        except Exception:
            result = "Invalid input"

    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
