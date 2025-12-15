from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud CI/CD Assignment – App Engine Deployment Successful"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
