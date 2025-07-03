from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your Deepseek API key from OpenRouter
OPENROUTER_API_KEY = "YOUR_API_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/api/ai/chat", methods=["POST"])
def ai_chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "ChatWA"
            },
            json={
                "model": "deepseek/deepseek-chat:free",
                "messages": [
                    {"role": "user", "content": user_message}
                ]
            }
        )

        result = response.json()

        if "choices" in result:
            reply = result["choices"][0]["message"]["content"]
            return jsonify({"reply": reply})
        else:
            return jsonify({"error": "Invalid response from OpenRouter.", "details": result}), 500

    except Exception as e:
        return jsonify({"error": "Request to AI failed.", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
