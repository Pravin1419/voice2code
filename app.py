from flask import Flask, render_template, request, jsonify
from code_generator import generate_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    text = data.get("text", "")

    code = generate_code(text)

    # Save file
    with open("generated_code.py", "w") as f:
        f.write(code)

    return jsonify({"code": code})

if __name__ == "__main__":
    app.run(debug=True)