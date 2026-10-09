from flask import Flask, request, jsonify
from ai_service import EduGenieAIService

app = Flask(__name__)
ai_engine = EduGenieAIService(api_key="YOUR_GEMINI_API_KEY")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    emotion = data.get("emotion", "neutral")
    
    bot_reply = ai_engine.generate_learning_response(user_message, emotion)
    return jsonify({"status": "success", "response": bot_reply})

if __name__ == '__main__':
    app.run(port=5000)