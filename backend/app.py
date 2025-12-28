from flask import Flask, request, jsonify
from flask_cors import CORS
import rules
from newspaper import Article

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Fake News Verification API is running!"

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    content = data.get('content', None)
    url = data.get('url', None)

    # Extract content from URL if text not provided
    if url and not content:
        try:
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
        except Exception as e:
            return jsonify({
                "error": "Failed to fetch content from URL",
                "details": str(e)
            }), 400

    if not content:
        return jsonify({"error": "No content or URL provided"}), 400

    score, reasons, summary = rules.evaluate_credibility(content, url)
    
    return jsonify({
        "score": score,
        "reasons": reasons,
        "summary": summary
    })

if __name__ == "__main__":
    app.run(debug=True, port=5001)
