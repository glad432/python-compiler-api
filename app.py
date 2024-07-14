import subprocess
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_code():
    code = request.data.decode("utf-8")
    try:
        process = subprocess.Popen(
            ["python"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        stdout, stderr = process.communicate(input=code, timeout=5)

        if process.returncode == 0:
            result = stdout
        else:
            result = f"Error: {stderr}"

    except subprocess.TimeoutExpired:
        result = "Timeout: The code took too long to execute."

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(debug=False)
