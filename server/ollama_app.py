from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify("hello from ollama")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt')
    print("prompt", prompt)
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    responses = []
    errors = []
    urls = [
        "http://localhost:11431/api/generate",
        "http://localhost:11434/api/generate",
        "http://localhost:11433/api/generate"
    ]
    models = [
        "llama3", 
        "phi3", 
        "mistral"
        ]

    for url, model in zip(urls, models):
        try:
            payload = {'model': model, 'prompt': prompt}
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                res_text = response.text.replace('}', '},').strip()
                if res_text.endswith(',,') or res_text.endswith('},'):
                    res_text = res_text[:-1]
                responses.append({
                    'model': model,
                    'resp':  '[' + res_text + ']'
                })
        except Exception as error:
            print(error)
            errors.append({'model': model, 'error': str(error)})

    return jsonify([responses, errors])

if __name__ == '__main__':
    app.run(port=5000)
