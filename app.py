from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "WE HELP OCR API Running ✅"

@app.route('/verify', methods=['POST'])
def verify():

    name = request.form.get("name")
    qualification = request.form.get("qualification")

    return jsonify({
        "status":"Verified",
        "score":95
    })

if __name__ == "__main__":
    app.run()
