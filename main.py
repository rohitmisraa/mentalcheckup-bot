from flask import Flask, request, jsonify

import chatbot

app = Flask(__name__)

@app.route("/chat/<question>")

def home(question):
    return chatbot.chat_bot(question), 200

if __name__ == "__main__":
    app.run(debug=True)