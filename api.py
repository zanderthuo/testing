from flask import Flask, request, jsonify
import requests
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# === Environment Variables ===
BASE_URL = os.environ.get("BASE_URL", "https://openrouter.ai/api/v1")
API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
DEFAULT_MODEL = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")  # fallback
PORT = int(os.environ.get("PORT", 5001))


def query(input_text, model_id):
    """Send a chat completion request to OpenRouter."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "dt1-25-demo",
    }

    url = f"{BASE_URL}/chat/completions"

    body = {
        "model": model_id or DEFAULT_MODEL,
        "messages": [{"role": "user", "content": input_text}],
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        logging.error(f"OpenRouter returned {response.status_code}: {response.text}")
        return {"error": response.text}
    except Exception as e:
        logging.error(f"OpenRouter API error: {e}")
        return {"error": str(e)}


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    input_text = data.get("input")
    model_id = data.get("model_id", DEFAULT_MODEL)

    if not input_text:
        return jsonify({"error": "Missing input text"}), 400

    response = query(input_text, model_id)

    answer = (
        response.get("choices", [{}])[0]
        .get("message", {})
        .get("content", "No response")
    )

    output = jsonify({"answer": answer})
    output.headers.add("Access-Control-Allow-Origin", "*")
    return output


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ack": "pong"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
