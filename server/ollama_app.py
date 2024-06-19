from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt')
    print(prompt)
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    res = []
    errors = []
    urls = [
        "http://localhost:11434/api/generate",
        "http://localhost:11434/api/generate",
        "http://localhost:11434/api/generate",
    ]
    models = ["llama3", "phi3", "mistral"]
    for i in [0,1,2]:
        url = urls[i]
        payload = {
            "model": models[i],
            "prompt": prompt
        }
        headers = {
            "Content-Type": "application/json"
        }
        print(prompt, models[i], "---------------------------------------------------------")
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            res.append({
                "model": models[i],
                "resp": response.json().get("text")
            })
        else:
            print(response.json())
            errors.append({
                "model": models[i],
                "error": response.text
            })
    return jsonify([res, errors])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
