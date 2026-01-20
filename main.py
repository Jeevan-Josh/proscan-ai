from google import genai
from flask import Flask, jsonify, request, render_template

client = genai.Client(api_key="AIzaSyDaYbQoMqGqmbv1bWTBQeCOHJvrgbSvDX8")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("message")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt   
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(port=8080, debug=True)